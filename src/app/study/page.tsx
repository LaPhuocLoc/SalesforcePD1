"use client";

import React, { useState, useEffect, useMemo, Suspense } from "react";
import QuestionCard from "@/components/QuestionCard";
import questionsDataRaw from "@/data/questions.json";
import { motion, AnimatePresence } from "framer-motion";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { useSearchParams } from "next/navigation";

function StudyPageContent() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answeredQuestions, setAnsweredQuestions] = useState<Record<number, boolean>>({});
  const [mounted, setMounted] = useState(false);
  const searchParams = useSearchParams();
  const setParam = searchParams.get("set");

  const questionsData = useMemo(() => {
    if (setParam === "0") {
      return questionsDataRaw.filter((q: any) => q.id >= 213);
    }
    return questionsDataRaw;
  }, [setParam]);

  useEffect(() => {
    setMounted(true);
    const storageKeySuffix = setParam === "0" ? "-set0" : "";
    const savedIndex = localStorage.getItem(`pd1-study-index${storageKeySuffix}`);
    if (savedIndex) {
      setCurrentIndex(parseInt(savedIndex, 10));
    }
    const savedAnswered = localStorage.getItem(`pd1-answered${storageKeySuffix}`);
    if (savedAnswered) {
      try {
        setAnsweredQuestions(JSON.parse(savedAnswered));
      } catch (e) {}
    }
  }, [setParam]);

  useEffect(() => {
    if (!mounted) return;
    const storageKeySuffix = setParam === "0" ? "-set0" : "";
    localStorage.setItem(`pd1-study-index${storageKeySuffix}`, currentIndex.toString());
  }, [currentIndex, mounted, setParam]);

  useEffect(() => {
    if (!mounted) return;
    const storageKeySuffix = setParam === "0" ? "-set0" : "";
    localStorage.setItem(`pd1-answered${storageKeySuffix}`, JSON.stringify(answeredQuestions));
  }, [answeredQuestions, mounted, setParam]);

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

  const handleAnswered = () => {
    setAnsweredQuestions(prev => ({ ...prev, [questionsData[currentIndex].id]: true }));
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
              question={questionsData[currentIndex] as any} 
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
          {questionsData.map((q: any, idx: number) => {
            const isCurrent = idx === currentIndex;
            const isAnswered = answeredQuestions[q.id];
            
            let btnStyle: React.CSSProperties = {
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
              backgroundColor: isAnswered ? 'var(--color-brand-cyan)' : 'var(--color-bg-surface)',
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
