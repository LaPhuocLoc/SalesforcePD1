"use client";

import React, { useState, useEffect, useCallback } from "react";
import Link from "next/link";
import { ArrowLeft, Clock, ArrowRight, CheckCircle2, XCircle, Lightbulb } from "lucide-react";
import questionsData from "@/data/questions.json";
import ExamQuestionCard from "@/components/ExamQuestionCard";
import FormattedText from "@/components/FormattedText";

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

export default function ExamPage() {
  const [examQuestions, setExamQuestions] = useState<Question[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState<Record<number, string[]>>({});
  const [timeLeft, setTimeLeft] = useState(105 * 60); // 105 minutes
  const [isFinished, setIsFinished] = useState(false);
  const [score, setScore] = useState(0);
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  useEffect(() => {
    // Pick 65 random questions
    const shuffled = [...(questionsData as unknown as Question[])].sort(() => 0.5 - Math.random());
    setExamQuestions(shuffled.slice(0, 65));
  }, []);

  // Navigation Guard - Tab close / Refresh
  useEffect(() => {
    if (isFinished) return;

    const handleBeforeUnload = (e: BeforeUnloadEvent) => {
      e.preventDefault();
      e.returnValue = '';
    };

    window.addEventListener('beforeunload', handleBeforeUnload);
    return () => window.removeEventListener('beforeunload', handleBeforeUnload);
  }, [isFinished]);

  // Navigation Guard - Browser Back / Popstate
  useEffect(() => {
    if (isFinished) return;

    const handlePopState = () => {
      if (!isFinished) {
        if (confirm("Bạn đang thi thử, có muốn thoát khỏi trang này không?")) {
          // Force hard reload to break out of history trap
          window.location.href = "/";
        } else {
          // Push current state back to keep user on page
          window.history.pushState(null, "", window.location.href);
        }
      }
    };

    window.history.pushState(null, "", window.location.href);
    window.addEventListener('popstate', handlePopState);
    return () => window.removeEventListener('popstate', handlePopState);
  }, [isFinished]);

  const finishExam = useCallback(() => {
    let newScore = 0;
    examQuestions.forEach(q => {
      const userAns = answers[q.id] || [];
      const correctAns = q.correct;
      if (userAns.length === correctAns.length && userAns.every(ans => correctAns.includes(ans))) {
        newScore++;
      }
    });
    setScore(newScore);
    setIsFinished(true);
    window.scrollTo(0, 0);
  }, [examQuestions, answers]);

  useEffect(() => {
    if (examQuestions.length === 0 || isFinished) return;
    
    const timer = setInterval(() => {
      setTimeLeft((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          finishExam();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [examQuestions, isFinished, finishExam]);

  const handleNext = () => {
    if (currentIndex < examQuestions.length - 1) {
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

  const formatTime = (seconds: number) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  const handleHeaderBack = () => {
    if (confirm("Bạn đang thi thử, có muốn thoát khỏi trang này không?")) {
      window.location.href = "/";
    }
  };

  if (!mounted || examQuestions.length === 0) {
    return <main className="container" style={{ padding: '4rem', textAlign: 'center' }}>Đang tải đề thi...</main>;
  }

  if (isFinished) {
    const percentage = Math.round((score / 65) * 100);
    const passed = percentage >= 68;
    const wrongCount = 65 - score;

    return (
      <main className="container" style={{ paddingBottom: '4rem', paddingTop: '2rem' }}>
        {/* SUMMARY SECTION */}
        <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
          <h1 style={{ fontSize: '2rem', marginBottom: '1rem', color: passed ? 'var(--color-success)' : 'var(--color-error)' }}>
            {passed ? '🎉 Chúc mừng bạn đã đậu!' : '❌ Bạn chưa đạt yêu cầu'}
          </h1>
          <div style={{ backgroundColor: 'var(--color-bg-surface)', padding: '2rem', borderRadius: 'var(--radius-xl)', border: '1px solid var(--color-border)', maxWidth: '600px', margin: '0 auto' }}>
            <div style={{ fontSize: '4rem', fontWeight: 'bold', color: passed ? 'var(--color-success)' : 'var(--color-error)', lineHeight: 1 }}>
              {percentage}%
            </div>
            <div style={{ display: 'flex', justifyContent: 'center', gap: '2rem', marginTop: '1.5rem' }}>
              <div style={{ textAlign: 'center' }}>
                <div style={{ fontSize: '0.875rem', color: 'var(--color-text-tertiary)' }}>Đúng</div>
                <div style={{ fontSize: '1.25rem', fontWeight: 'bold', color: 'var(--color-success)' }}>{score}</div>
              </div>
              <div style={{ textAlign: 'center' }}>
                <div style={{ fontSize: '0.875rem', color: 'var(--color-text-tertiary)' }}>Sai / Chưa làm</div>
                <div style={{ fontSize: '1.25rem', fontWeight: 'bold', color: 'var(--color-error)' }}>{wrongCount}</div>
              </div>
              <div style={{ textAlign: 'center' }}>
                <div style={{ fontSize: '0.875rem', color: 'var(--color-text-tertiary)' }}>Tổng câu</div>
                <div style={{ fontSize: '1.25rem', fontWeight: 'bold' }}>65</div>
              </div>
            </div>
            
            <div style={{ marginTop: '2rem', display: 'flex', justifyContent: 'center', gap: '2rem', paddingTop: '1.5rem', borderTop: '1px solid var(--color-border)' }}>
              <div style={{ textAlign: 'center' }}>
                <div style={{ fontSize: '0.875rem', color: 'var(--color-text-tertiary)' }}>Thời gian làm bài</div>
                <div style={{ fontSize: '1.25rem', fontWeight: 'bold' }}>{formatTime((105 * 60) - timeLeft)}</div>
              </div>
              <div style={{ textAlign: 'center' }}>
                <div style={{ fontSize: '0.875rem', color: 'var(--color-text-tertiary)' }}>Điểm qua môn</div>
                <div style={{ fontSize: '1.25rem', fontWeight: 'bold' }}>68%</div>
              </div>
            </div>
          </div>
          
          <div style={{ marginTop: '2rem' }}>
            <Link href="/" className="btn-primary" style={{ display: 'inline-flex', textDecoration: 'none' }}>
              Về trang chủ
            </Link>
          </div>
        </div>

        {/* NAVIGATION GRID - COLORED */}
        <section style={{ marginBottom: '4rem', maxWidth: '900px', margin: '0 auto 4rem auto' }}>
          <h3 style={{ marginBottom: '1.5rem', fontSize: '1.25rem', color: 'var(--color-text-primary)' }}>Bảng kết quả chi tiết</h3>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(40px, 1fr))', gap: '8px' }}>
            {examQuestions.map((q, idx) => {
              const userAns = answers[q.id] || [];
              const correctAns = q.correct;
              const isCorrect = userAns.length === correctAns.length && userAns.every(ans => correctAns.includes(ans));
              
              return (
                <a 
                  key={q.id} 
                  href={`#question-${idx}`}
                  style={{
                    padding: '0.5rem 0',
                    textAlign: 'center',
                    borderRadius: 'var(--radius-md)',
                    fontSize: '0.875rem',
                    fontWeight: 'bold',
                    textDecoration: 'none',
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    backgroundColor: isCorrect ? 'var(--color-success)' : 'var(--color-error)',
                    color: '#ffffff',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    height: '40px',
                    opacity: 0.9,
                    transition: 'opacity 0.2s'
                  }}
                  onMouseOver={(e) => e.currentTarget.style.opacity = '1'}
                  onMouseOut={(e) => e.currentTarget.style.opacity = '0.9'}
                >
                  {idx + 1}
                </a>
              );
            })}
          </div>
        </section>

        {/* DETAILED QUESTIONS LIST */}
        <section style={{ display: 'flex', flexDirection: 'column', gap: '3rem', maxWidth: '900px', margin: '0 auto' }}>
          {examQuestions.map((q, idx) => {
            const userAns = answers[q.id] || [];
            const correctAns = q.correct;
            const isCorrect = userAns.length === correctAns.length && userAns.every(ans => correctAns.includes(ans));
            
            return (
              <div key={q.id} id={`question-${idx}`} style={{ backgroundColor: 'var(--color-bg-surface)', padding: '2rem', borderRadius: 'var(--radius-xl)', border: `2px solid ${isCorrect ? 'var(--color-success)' : 'var(--color-error)'}` }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1.5rem', alignItems: 'flex-start' }}>
                  <h3 style={{ margin: 0, color: 'var(--color-text-primary)' }}>Câu hỏi #{idx + 1}</h3>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: isCorrect ? 'var(--color-success)' : 'var(--color-error)', fontWeight: 'bold', backgroundColor: isCorrect ? 'var(--color-success-bg)' : 'var(--color-error-bg)', padding: '0.5rem 1rem', borderRadius: 'var(--radius-full)' }}>
                    {isCorrect ? <><CheckCircle2 size={18} /> Đúng</> : <><XCircle size={18} /> Sai</>}
                  </div>
                </div>

                <div className="question-text" style={{ marginBottom: '1.5rem' }}>
                  <FormattedText text={q.question} />
                </div>

                <div className="options-list" style={{ marginBottom: '2rem' }}>
                  {q.options.map((opt) => {
                    const isSelected = userAns.includes(opt.key);
                    const isActualCorrect = correctAns.includes(opt.key);
                    
                    let classes = "option-button";
                    if (isActualCorrect) classes += " correct";
                    else if (isSelected) classes += " incorrect";
                    
                    return (
                      <div key={opt.key} className={classes} style={{ opacity: 1, cursor: 'default' }}>
                        <span className="option-key">{opt.key}</span>
                        <span className="option-text">
                          <FormattedText text={opt.text} isOption={true} />
                        </span>
                        {isActualCorrect && <CheckCircle2 size={20} color="var(--color-success)" style={{ marginLeft: 'auto', flexShrink: 0 }} />}
                        {isSelected && !isActualCorrect && <XCircle size={20} color="var(--color-error)" style={{ marginLeft: 'auto', flexShrink: 0 }} />}
                      </div>
                    );
                  })}
                </div>

                {/* Explanation */}
                <div className="explanation-section" style={{ marginTop: '1rem', borderTop: '1px solid var(--color-border)', paddingTop: '2rem' }}>
                  <h4 style={{ margin: '0 0 1.5rem 0', fontSize: '1.125rem', color: 'var(--color-text-primary)' }}>Giải thích chi tiết</h4>
                  
                  <div className="explanation-block" style={{ marginBottom: '1.5rem' }}>
                    <h5 style={{ color: 'var(--color-text-secondary)', marginBottom: '0.5rem', fontSize: '1rem', margin: 0 }}>Dịch câu hỏi</h5>
                    <div className="explanation-content" style={{ marginTop: '0.5rem' }}>
                      <FormattedText text={q.explanation.vi_question} />
                    </div>
                  </div>

                  <div className="explanation-block" style={{ marginBottom: '1.5rem' }}>
                    <div className="explanation-title" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--color-brand-cyan)', fontWeight: '600', marginBottom: '0.5rem' }}>
                      <CheckCircle2 size={18} /> Tại sao đúng?
                    </div>
                    <div className="explanation-content">
                      <FormattedText text={q.explanation.why_correct} />
                    </div>
                  </div>

                  {q.explanation.why_wrong && Object.keys(q.explanation.why_wrong).length > 0 && (
                    <div className="explanation-block" style={{ marginBottom: '1.5rem' }}>
                      <div className="explanation-title" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--color-error)', fontWeight: '600', marginBottom: '0.5rem' }}>
                        <XCircle size={18} /> Tại sao các đáp án khác sai?
                      </div>
                      <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
                        {Object.entries(q.explanation.why_wrong).map(([key, reason]) => (
                          <li key={key} style={{ marginBottom: '1rem' }}>
                            <strong style={{ color: 'var(--color-error)' }}>{key}:</strong>
                            <div style={{ marginTop: '0.5rem' }} className="explanation-content">
                              <FormattedText text={reason} />
                            </div>
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}

                  {q.explanation.tip && (
                    <div className="tip-box" style={{ marginTop: '1.5rem', backgroundColor: 'rgba(245, 158, 11, 0.1)', padding: '1.5rem', borderRadius: 'var(--radius-lg)', border: '1px solid rgba(245, 158, 11, 0.2)' }}>
                      <div className="explanation-title" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--color-warning)', fontWeight: '600', marginBottom: '0.5rem' }}>
                        <Lightbulb size={18} /> Mẹo ghi nhớ (Tip)
                      </div>
                      <div className="explanation-content" style={{ color: 'var(--color-warning)' }}>
                        <FormattedText text={q.explanation.tip} />
                      </div>
                    </div>
                  )}
                </div>

              </div>
            );
          })}
        </section>
        
        <div style={{ textAlign: 'center', marginTop: '3rem' }}>
          <button onClick={() => window.scrollTo(0, 0)} className="btn-secondary" style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem' }}>
            Cuộn lên đầu trang
          </button>
        </div>
      </main>
    );
  }

  const currentQ = examQuestions[currentIndex];

  return (
    <main className="container" style={{ paddingBottom: '4rem', paddingTop: '1rem' }}>
      <header style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1.5rem', backgroundColor: 'var(--color-bg-surface)', padding: '1rem 1.5rem', borderRadius: 'var(--radius-lg)', border: '1px solid var(--color-border)', position: 'sticky', top: '1rem', zIndex: 10 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
          <button 
            onClick={handleHeaderBack}
            style={{ color: 'var(--color-text-tertiary)', background: 'none', border: 'none', cursor: 'pointer', display: 'flex', alignItems: 'center' }}
          >
            <ArrowLeft size={20} />
          </button>
          <div style={{ fontWeight: '600' }}>Câu {currentIndex + 1}/65</div>
        </div>
        
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: timeLeft < 600 ? 'var(--color-error)' : 'var(--color-brand-cyan)', fontWeight: 'bold', fontSize: '1.25rem' }}>
          <Clock size={20} />
          {formatTime(timeLeft)}
        </div>
        
        <button 
          onClick={() => {
            if (confirm("Bạn có chắc chắn muốn nộp bài?")) finishExam();
          }}
          style={{ 
            backgroundColor: 'var(--color-success)', 
            color: 'var(--color-bg-base)', 
            padding: '0.625rem 1.25rem', 
            borderRadius: 'var(--radius-md)', 
            fontWeight: 'bold',
            transition: 'all 0.2s',
            boxShadow: '0 0 15px rgba(16, 185, 129, 0.3)'
          }}
          onMouseOver={(e) => e.currentTarget.style.backgroundColor = '#059669'}
          onMouseOut={(e) => e.currentTarget.style.backgroundColor = 'var(--color-success)'}
        >
          Nộp bài
        </button>
      </header>

      <div style={{ minHeight: '400px' }}>
        <ExamQuestionCard 
          question={currentQ}
          selectedKeys={answers[currentQ.id] || []}
          onChange={(keys) => setAnswers(prev => ({ ...prev, [currentQ.id]: keys }))}
        />
      </div>

      <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: '2rem' }}>
        <button 
          className="btn-secondary" 
          onClick={handlePrevious} 
          disabled={currentIndex === 0}
          style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}
        >
          <ArrowLeft size={18} /> Trước
        </button>
        
        {currentIndex === examQuestions.length - 1 ? (
          <button 
            className="btn-primary" 
            onClick={() => {
              if (confirm("Bạn có chắc chắn muốn nộp bài?")) finishExam();
            }}
            style={{ 
              display: 'flex', 
              alignItems: 'center', 
              gap: '0.5rem', 
              backgroundColor: 'var(--color-success)',
              color: 'var(--color-bg-base)'
            }}
          >
            Nộp bài <CheckCircle2 size={18} />
          </button>
        ) : (
          <button 
            className="btn-primary" 
            onClick={handleNext} 
            style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}
          >
            Tiếp <ArrowRight size={18} />
          </button>
        )}
      </div>

      <section style={{ marginTop: '3rem', borderTop: '1px solid var(--color-border)', paddingTop: '2rem' }}>
        <h3 style={{ marginBottom: '1.5rem', fontSize: '1rem', color: 'var(--color-text-secondary)' }}>Bảng câu hỏi ({Object.keys(answers).filter(k => answers[parseInt(k)].length > 0).length}/65)</h3>
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(40px, 1fr))', gap: '8px' }}>
          {examQuestions.map((q, idx) => {
            const isCurrent = idx === currentIndex;
            const isAnswered = answers[q.id] && answers[q.id].length > 0;
            
            return (
              <div 
                key={q.id} 
                onClick={() => {
                  setCurrentIndex(idx);
                  window.scrollTo(0, 0);
                }}
                style={{
                  padding: '0.5rem 0',
                  textAlign: 'center',
                  borderRadius: 'var(--radius-md)',
                  fontSize: '0.875rem',
                  fontWeight: isCurrent ? 'bold' : 'normal',
                  cursor: 'pointer',
                  border: isCurrent ? '2px solid var(--color-brand-cyan)' : (isAnswered ? '1px solid transparent' : '1px solid var(--color-border)'),
                  backgroundColor: isAnswered ? 'var(--color-brand-cyan)' : 'var(--color-bg-surface)',
                  color: isAnswered ? '#ffffff' : (isCurrent ? 'var(--color-brand-cyan)' : 'var(--color-text-secondary)'),
                  transition: 'all 0.2s',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  height: '40px'
                }}
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
