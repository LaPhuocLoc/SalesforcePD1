"use client";

import React, { useState, useEffect, useMemo, useRef, Suspense } from "react";
import QuestionCard from "@/components/QuestionCard";
import questionsDataRaw from "@/data/questions.json";
import questionsDataEnhanced from "@/data/questions_enhanced.json";
import { motion, AnimatePresence } from "framer-motion";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { useSearchParams } from "next/navigation";

interface Option {
  key: string;
  text: string;
}

interface Explanation {
  vi_question: string;
  why_correct: string;
  why_wrong: Record<string, string>;
  tip: string;
}

interface Question {
  id: number;
  question: string;
  options: Option[];
  correct: string[];
  type: string;
  explanation: Explanation;
}

type QuestionResult = "correct" | "incorrect";
type StoredQuestionResult = QuestionResult | boolean;

interface StudyProgress {
  currentIndex: number;
  answered: Record<number, StoredQuestionResult>;
  updatedAt: string;
}

interface ProgressData {
  study?: Record<string, StudyProgress>;
}

const progressSyncTimeoutMs = 3000;

const getStorageKeySuffix = (sourceParam: string | null, setParam: string | null) =>
  (sourceParam === "enhanced" ? "-enhanced" : "") + (setParam === "0" ? "-set0" : "");

const getProgressScope = (sourceParam: string | null, setParam: string | null) => {
  const source = sourceParam === "enhanced" ? "enhanced" : "default";
  const set = setParam === "0" ? "set0" : "all";
  return `${source}-${set}`;
};

const getProgressHeaders = () => {
  const headers: Record<string, string> = {
    "Content-Type": "application/json",
  };
  const key = process.env.NEXT_PUBLIC_PROGRESS_KEY;
  if (key) headers["x-progress-key"] = key;
  return headers;
};

const parseAnswered = (value: string | null): Record<number, StoredQuestionResult> => {
  if (!value) return {};
  try {
    return JSON.parse(value) as Record<number, StoredQuestionResult>;
  } catch {
    return {};
  }
};

const isRemoteNewer = (remoteUpdatedAt?: string, localUpdatedAt?: string | null) => {
  if (!remoteUpdatedAt) return false;
  if (!localUpdatedAt) return true;
  return new Date(remoteUpdatedAt).getTime() > new Date(localUpdatedAt).getTime();
};

function StudyPageContent() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answeredQuestions, setAnsweredQuestions] = useState<Record<number, StoredQuestionResult>>({});
  const [mounted, setMounted] = useState(false);
  const searchParams = useSearchParams();
  const setParam = searchParams.get("set");
  const sourceParam = searchParams.get("source");
  const progressStoreRef = useRef<ProgressData>({ study: {} });
  const readyToSyncRef = useRef(false);
  const storageKeySuffix = useMemo(() => getStorageKeySuffix(sourceParam, setParam), [sourceParam, setParam]);
  const progressScope = useMemo(() => getProgressScope(sourceParam, setParam), [sourceParam, setParam]);

  const questionsData = useMemo<Question[]>(() => {
    const dataSrc = (sourceParam === "enhanced" ? questionsDataEnhanced : questionsDataRaw) as unknown as Question[];
    if (setParam === "0") {
      return dataSrc.filter((q) => q.id >= 213);
    }
    return dataSrc;
  }, [setParam, sourceParam]);

  useEffect(() => {
    let cancelled = false;
    readyToSyncRef.current = false;

    const loadProgress = async () => {
      const savedIndex = localStorage.getItem(`pd1-study-index${storageKeySuffix}`);
      const savedAnswered = localStorage.getItem(`pd1-answered${storageKeySuffix}`);
      const localUpdatedAt = localStorage.getItem(`pd1-study-updated${storageKeySuffix}`);

      let nextIndex = savedIndex ? parseInt(savedIndex, 10) : 0;
      let nextAnswered = parseAnswered(savedAnswered);

      const controller = new AbortController();
      const timeout = window.setTimeout(() => controller.abort(), progressSyncTimeoutMs);

      try {
        const response = await fetch("/api/progress", {
          cache: "no-store",
          headers: getProgressHeaders(),
          signal: controller.signal,
        });
        if (response.ok) {
          const data = (await response.json()) as { progress?: ProgressData };
          const progress = data.progress || { study: {} };
          progressStoreRef.current = progress;

          const remoteProgress = progress.study?.[progressScope];
          if (remoteProgress && isRemoteNewer(remoteProgress.updatedAt, localUpdatedAt)) {
            nextIndex = remoteProgress.currentIndex;
            nextAnswered = remoteProgress.answered || {};
          }
        }
      } catch {
        // localStorage remains the offline fallback.
      } finally {
        window.clearTimeout(timeout);
      }

      if (cancelled) return;

      const maxIndex = Math.max(questionsData.length - 1, 0);
      const clampedIndex = Math.min(Math.max(Number.isFinite(nextIndex) ? nextIndex : 0, 0), maxIndex);
      setCurrentIndex(clampedIndex);
      setAnsweredQuestions(nextAnswered);
      readyToSyncRef.current = true;
      setMounted(true);
    };

    void loadProgress();

    return () => {
      cancelled = true;
    };
  }, [progressScope, questionsData.length, storageKeySuffix]);

  useEffect(() => {
    if (!mounted || !readyToSyncRef.current) return;

    const updatedAt = new Date().toISOString();
    const studyProgress: StudyProgress = {
      currentIndex,
      answered: answeredQuestions,
      updatedAt,
    };

    localStorage.setItem(`pd1-study-index${storageKeySuffix}`, currentIndex.toString());
    localStorage.setItem(`pd1-answered${storageKeySuffix}`, JSON.stringify(answeredQuestions));
    localStorage.setItem(`pd1-study-updated${storageKeySuffix}`, updatedAt);

    progressStoreRef.current = {
      ...progressStoreRef.current,
      study: {
        ...progressStoreRef.current.study,
        [progressScope]: studyProgress,
      },
    };

    const timer = window.setTimeout(() => {
      void fetch("/api/progress", {
        method: "POST",
        headers: getProgressHeaders(),
        body: JSON.stringify({ progress: progressStoreRef.current }),
      }).catch(() => {
        // GitHub sync is best effort; localStorage has already been updated.
      });
    }, 1000);

    return () => window.clearTimeout(timer);
  }, [answeredQuestions, currentIndex, mounted, progressScope, storageKeySuffix]);

  const handleNext = () => {
    if (currentIndex < questionsData.length - 1) {
      setCurrentIndex(currentIndex + 1);
      window.scrollTo(0, 0);
    }
  };

  const handlePrevious = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
      window.scrollTo(0, 0);
    }
  };

  const handleAnswered = (isCorrect: boolean) => {
    setAnsweredQuestions(prev => ({
      ...prev,
      [questionsData[currentIndex].id]: isCorrect ? "correct" : "incorrect",
    }));
  };

  if (!mounted) {
    return <main className="container" style={{ padding: '4rem', textAlign: 'center' }}>Đang tải...</main>;
  }

  if (questionsData.length === 0) {
     return <main className="container" style={{ padding: '4rem', textAlign: 'center' }}>Không tìm thấy câu hỏi nào.</main>;
  }

  return (
    <main className="container" style={{ paddingBottom: '4rem', paddingTop: '1rem' }}>
      <div style={{ marginBottom: '1.5rem' }}>
        <Link href="/" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', color: 'var(--color-text-tertiary)', textDecoration: 'none', fontWeight: '500' }}>
          <ArrowLeft size={16} /> Quay lại
        </Link>
      </div>

      <div style={{ minHeight: '600px' }}>
        <AnimatePresence mode="wait">
          <motion.div
            key={questionsData[currentIndex].id}
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.2 }}
          >
            <QuestionCard 
              question={questionsData[currentIndex]} 
              onNext={handleNext}
              onPrevious={handlePrevious}
              isFirst={currentIndex === 0}
              isLast={currentIndex === questionsData.length - 1}
              onAnswered={handleAnswered}
            />
          </motion.div>
        </AnimatePresence>
      </div>

      <section style={{ maxWidth: '900px', margin: '3rem auto 0' }}>
        <h3 style={{ marginBottom: '1.5rem', fontSize: '1.25rem', color: 'var(--color-text-primary)' }}>Trạng thái câu hỏi ({Object.keys(answeredQuestions).length}/{questionsData.length})</h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(40px, 1fr))', gap: '8px' }}>
          {questionsData.map((q, idx) => {
            const isCurrent = idx === currentIndex;
            const questionResult = answeredQuestions[q.id];
            const isAnswered = Boolean(questionResult);
            const isIncorrect = questionResult === "incorrect";
            
            const btnStyle: React.CSSProperties = {
              padding: '0.5rem 0',
              textAlign: 'center',
              borderRadius: 'var(--radius-md)',
              fontSize: '0.875rem',
              fontWeight: isCurrent ? 'bold' : 'normal',
              cursor: 'pointer',
              border: isCurrent 
                ? '2px solid var(--color-brand-cyan)' 
                : isAnswered 
                  ? '1px solid transparent' 
                  : '1px solid var(--color-border)',
              backgroundColor: isIncorrect
                ? 'var(--color-error)'
                : isAnswered
                  ? 'var(--color-brand-cyan)'
                  : 'var(--color-bg-surface)',
              color: isAnswered ? '#ffffff' : (isCurrent ? 'var(--color-brand-cyan)' : 'var(--color-text-secondary)'),
              transition: 'all 0.2s',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              height: '40px'
            };

            return (
              <div 
                key={q.id} 
                onClick={() => {
                  setCurrentIndex(idx);
                  window.scrollTo(0, 0);
                }}
                style={btnStyle}
                title={`Câu hỏi ${q.id}`}
              >
                {idx + 1}
              </div>
            );
          })}
        </div>
      </section>
    </main>
  );
}

export default function StudyPage() {
  return (
    <Suspense fallback={<main className="container" style={{ padding: '4rem', textAlign: 'center' }}>Đang tải...</main>}>
      <StudyPageContent />
    </Suspense>
  );
}
