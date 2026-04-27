"use client";

import React, { useState } from "react";
import Link from "next/link";
import { CheckCircle2, XCircle, Lightbulb, ArrowRight, ArrowLeft, RotateCcw } from "lucide-react";
import FormattedText from "./FormattedText";

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

interface QuestionCardProps {
  question: Question;
  onNext: () => void;
  onPrevious: () => void;
  isFirst: boolean;
  isLast: boolean;
  onAnswered?: () => void;
}

export default function QuestionCard({
  question,
  onNext,
  onPrevious,
  isFirst,
  isLast,
  onAnswered
}: QuestionCardProps) {
  const [selectedKeys, setSelectedKeys] = useState<string[]>([]);
  const [showResult, setShowResult] = useState(false);

  const handleOptionClick = (key: string) => {
    if (showResult) return;

    if (question.type === "single") {
      setSelectedKeys([key]);
    } else {
      setSelectedKeys((prev) =>
        prev.includes(key) ? prev.filter((k) => k !== key) : [...prev, key]
      );
    }
  };

  const handleSubmit = () => {
    if (selectedKeys.length === 0) return;
    setShowResult(true);
    if (onAnswered) onAnswered();
  };

  const handleReset = () => {
    setSelectedKeys([]);
    setShowResult(false);
  };

  const isCorrect = (key: string) => question.correct.includes(key);
  const isSelected = (key: string) => selectedKeys.includes(key);

  const getOptionClass = (key: string) => {
    let classes = "option-button";
    if (isSelected(key)) classes += " selected";
    if (showResult) {
      if (isCorrect(key)) classes += " correct";
      else if (isSelected(key)) classes += " incorrect";
    }
    return classes;
  };

  return (
    <div className="study-card-container">
      <div className="study-card-face">
        {/* Header */}
        <div className="question-header" style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem' }}>
          <span style={{ color: 'var(--color-brand-cyan)', fontWeight: '600' }}>Câu hỏi #{question.id}</span>
          <span style={{ color: 'var(--color-text-tertiary)', fontSize: '0.875rem' }}>
            {question.type === 'single' ? 'Chọn 1 đáp án' : `Chọn ${question.correct.length} đáp án`}
          </span>
        </div>
        
        {/* Question Text */}
        <div className="question-text">
          <FormattedText text={question.question} />
        </div>

        {/* Options */}
        <div className="options-list">
          {question.options.map((option) => (
            <button
              key={option.key}
              className={getOptionClass(option.key)}
              onClick={() => handleOptionClick(option.key)}
              disabled={showResult}
            >
              <span className="option-key">{option.key}</span>
              <span className="option-text">
                <FormattedText text={option.text} isOption={true} />
              </span>
              {showResult && isCorrect(option.key) && (
                <CheckCircle2 size={20} color="var(--color-success)" style={{ marginLeft: 'auto', flexShrink: 0 }} />
              )}
              {showResult && isSelected(option.key) && !isCorrect(option.key) && (
                <XCircle size={20} color="var(--color-error)" style={{ marginLeft: 'auto', flexShrink: 0 }} />
              )}
            </button>
          ))}
        </div>

        {/* Inline Explanation Section */}
        {showResult && (
          <div className="explanation-section" style={{ marginTop: '1rem', borderTop: '1px solid var(--color-border)', paddingTop: '2rem' }}>
            <h3 style={{ margin: '0 0 1.5rem 0', fontSize: '1.25rem', color: 'var(--color-text-primary)' }}>Giải thích chi tiết</h3>
            
            <div className="explanation-block" style={{ marginBottom: '1.5rem' }}>
              <h4 style={{ color: 'var(--color-text-secondary)', marginBottom: '0.5rem', fontSize: '1rem' }}>Dịch câu hỏi</h4>
              <div className="explanation-content">
                <FormattedText text={question.explanation.vi_question} />
              </div>
            </div>

            <div className="explanation-block" style={{ marginBottom: '1.5rem' }}>
              <div className="explanation-title" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--color-brand-cyan)', fontWeight: '600', marginBottom: '0.5rem' }}>
                <CheckCircle2 size={18} /> Tại sao đúng?
              </div>
              <div className="explanation-content">
                <FormattedText text={question.explanation.why_correct} />
              </div>
            </div>

            {Object.keys(question.explanation.why_wrong).length > 0 && (
              <div className="explanation-block" style={{ marginBottom: '1.5rem' }}>
                <div className="explanation-title" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--color-error)', fontWeight: '600', marginBottom: '0.5rem' }}>
                  <XCircle size={18} /> Tại sao các đáp án khác sai?
                </div>
                <ul style={{ listStyle: 'none', padding: 0, margin: 0 }}>
                  {Object.entries(question.explanation.why_wrong).map(([key, reason]) => (
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

            {question.explanation.tip && (
              <div className="tip-box" style={{ marginTop: '1.5rem', backgroundColor: 'rgba(234, 179, 8, 0.1)', padding: '1.5rem', borderRadius: 'var(--radius-lg)', border: '1px solid rgba(234, 179, 8, 0.2)' }}>
                <div className="explanation-title" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--color-warning)', fontWeight: '600', marginBottom: '0.5rem' }}>
                  <Lightbulb size={18} /> Mẹo ghi nhớ (Tip)
                </div>
                <div className="explanation-content" style={{ color: 'var(--color-warning)' }}>
                  <FormattedText text={question.explanation.tip} />
                </div>
              </div>
            )}
          </div>
        )}

        {/* Unified Bottom Navigation & Actions */}
        <div style={{ marginTop: '2rem', display: 'flex', justifyContent: 'space-between', width: '100%', alignItems: 'center', gap: '1rem', flexWrap: 'wrap' }}>
          <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
            <button 
              className="btn-secondary" 
              onClick={() => { onPrevious(); handleReset(); }} 
              disabled={isFirst}
              style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.75rem 1rem' }}
            >
              <ArrowLeft size={18} />
              <span>Trước</span>
            </button>
            
            {!showResult ? (
              <button 
                className="btn-primary" 
                onClick={handleSubmit}
                disabled={selectedKeys.length !== question.correct.length}
                style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.75rem 1rem' }}
              >
                <CheckCircle2 size={18} />
                <span>Kiểm tra đáp án</span>
              </button>
            ) : (
              <button 
                className="btn-secondary" 
                onClick={handleReset}
                style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.75rem 1rem' }}
              >
                <RotateCcw size={18} />
                <span>Làm lại</span>
              </button>
            )}
          </div>

          {isLast ? (
            <Link 
              href="/"
              className="btn-primary" 
              style={{ 
                display: 'flex', 
                alignItems: 'center', 
                gap: '0.5rem', 
                padding: '0.75rem 1rem', 
                textDecoration: 'none',
                backgroundColor: 'var(--color-success)',
                color: 'var(--color-bg-base)'
              }}
            >
              <span>Hoàn thành</span>
              <CheckCircle2 size={18} />
            </Link>
          ) : (
            <button 
              className="btn-primary" 
              onClick={() => { onNext(); handleReset(); }} 
              style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', padding: '0.75rem 1rem' }}
            >
              <span>Tiếp</span>
              <ArrowRight size={18} />
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
