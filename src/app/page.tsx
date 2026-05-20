"use client";

import React, { useState } from "react";
import Link from "next/link";
import { ArrowRight, BookOpen, Sparkles } from "lucide-react";

export default function HomePage() {
  const [selectedMode, setSelectedMode] = useState<
    "exam" | "study" | "study_set0" | "exam_enhanced" | "study_enhanced"
  >("study_enhanced");

  const getHref = () => {
    switch (selectedMode) {
      case "exam":
        return "/exam";
      case "exam_enhanced":
        return "/exam?source=enhanced";
      case "study_set0":
        return "/study?set=0";
      case "study_enhanced":
        return "/study?source=enhanced";
      default:
        return "/study";
    }
  };

  const getButtonText = () => {
    if (selectedMode.startsWith("exam")) {
      return "Bắt đầu thi thử";
    }
    return "Bắt đầu ôn tập";
  };

  return (
    <main className="container" style={{ paddingBottom: '4rem', paddingTop: '4rem', maxWidth: '650px' }}>
      <div style={{ marginBottom: '2.5rem', textAlign: 'center' }}>
        <h1 style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.75rem', fontSize: '2.25rem', marginBottom: '0.75rem', color: 'var(--color-text-primary)' }}>
          🎓 Salesforce PD1 Prep
        </h1>
        <p style={{ color: 'var(--color-text-secondary)', fontSize: '1.125rem', margin: 0 }}>
          Hệ thống luyện thi Platform Developer I chất lượng cao
        </p>
      </div>

      {/* CATEGORY: ENHANCED DATASET */}
      <div style={{ marginBottom: '2rem' }}>
        <h2 style={{ fontSize: '1.1rem', textTransform: 'uppercase', letterSpacing: '0.05em', color: 'var(--color-brand-cyan)', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <Sparkles size={16} /> Bộ Đề Mới Làm Giàu (349 Câu - 2026)
        </h2>
        
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          {/* Study Enhanced */}
          <div 
            onClick={() => setSelectedMode("study_enhanced")}
            style={{
              padding: '1.25rem 1.5rem',
              borderRadius: 'var(--radius-lg)',
              border: selectedMode === "study_enhanced" ? '2px solid var(--color-brand-cyan)' : '1px solid var(--color-border)',
              backgroundColor: selectedMode === "study_enhanced" ? 'rgba(6, 182, 212, 0.05)' : 'var(--color-bg-surface)',
              cursor: 'pointer',
              transition: 'all 0.2s',
              display: 'flex',
              alignItems: 'flex-start',
              gap: '1rem'
            }}
          >
            <div style={{ fontSize: '1.5rem', marginTop: '0.25rem' }}>🚀</div>
            <div>
              <h3 style={{ margin: '0 0 0.25rem 0', fontSize: '1.125rem', color: 'var(--color-text-primary)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                Ôn tập Nâng cao (349 câu) <span style={{ fontSize: '0.75rem', backgroundColor: 'var(--color-brand-cyan)', color: 'white', padding: '2px 8px', borderRadius: '4px' }}>MỚI</span>
              </h3>
              <p style={{ margin: 0, color: 'var(--color-text-secondary)', fontSize: '0.875rem', lineHeight: '1.4' }}>
                Đầy đủ giải thích cực kỳ chi tiết từng đáp án Đúng/Sai và Mẹo thi (Tip) bằng Tiếng Việt.
              </p>
            </div>
          </div>

          {/* Exam Enhanced */}
          <div 
            onClick={() => setSelectedMode("exam_enhanced")}
            style={{
              padding: '1.25rem 1.5rem',
              borderRadius: 'var(--radius-lg)',
              border: selectedMode === "exam_enhanced" ? '2px solid var(--color-brand-cyan)' : '1px solid var(--color-border)',
              backgroundColor: selectedMode === "exam_enhanced" ? 'rgba(6, 182, 212, 0.05)' : 'var(--color-bg-surface)',
              cursor: 'pointer',
              transition: 'all 0.2s',
              display: 'flex',
              alignItems: 'flex-start',
              gap: '1rem'
            }}
          >
            <div style={{ fontSize: '1.5rem', marginTop: '0.25rem' }}>🎯</div>
            <div>
              <h3 style={{ margin: '0 0 0.25rem 0', fontSize: '1.125rem', color: 'var(--color-text-primary)' }}>
                Thi thử Bộ Đề Mới (65 câu random)
              </h3>
              <p style={{ margin: 0, color: 'var(--color-text-secondary)', fontSize: '0.875rem', lineHeight: '1.4' }}>
                Sinh đề thi ngẫu nhiên từ kho 349 câu nâng cao. 105 phút, điều kiện đạt là &gt;= 68%.
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* CATEGORY: ORIGINAL DATASET */}
      <div style={{ marginBottom: '2.5rem' }}>
        <h2 style={{ fontSize: '1.1rem', textTransform: 'uppercase', letterSpacing: '0.05em', color: 'var(--color-text-tertiary)', marginBottom: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
          <BookOpen size={16} /> Bộ Đề Cũ (Original)
        </h2>
        
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
          {/* Study Original */}
          <div 
            onClick={() => setSelectedMode("study")}
            style={{
              padding: '1.25rem 1.5rem',
              borderRadius: 'var(--radius-lg)',
              border: selectedMode === "study" ? '2px solid var(--color-brand-cyan)' : '1px solid var(--color-border)',
              backgroundColor: selectedMode === "study" ? 'rgba(6, 182, 212, 0.05)' : 'var(--color-bg-surface)',
              cursor: 'pointer',
              transition: 'all 0.2s',
              display: 'flex',
              alignItems: 'flex-start',
              gap: '1rem',
              opacity: 0.85
            }}
          >
            <div style={{ fontSize: '1.5rem', marginTop: '0.25rem' }}>📖</div>
            <div>
              <h3 style={{ margin: '0 0 0.25rem 0', fontSize: '1.125rem', color: 'var(--color-text-primary)' }}>
                Ôn tập Bộ đề cũ (272 câu)
              </h3>
              <p style={{ margin: 0, color: 'var(--color-text-secondary)', fontSize: '0.875rem', lineHeight: '1.4' }}>
                Làm toàn bộ 272 câu hỏi của phiên bản cũ. Không giới hạn thời gian.
              </p>
            </div>
          </div>

          {/* Study Set 0 */}
          <div 
            onClick={() => setSelectedMode("study_set0")}
            style={{
              padding: '1.25rem 1.5rem',
              borderRadius: 'var(--radius-lg)',
              border: selectedMode === "study_set0" ? '2px solid var(--color-brand-cyan)' : '1px solid var(--color-border)',
              backgroundColor: selectedMode === "study_set0" ? 'rgba(6, 182, 212, 0.05)' : 'var(--color-bg-surface)',
              cursor: 'pointer',
              transition: 'all 0.2s',
              display: 'flex',
              alignItems: 'flex-start',
              gap: '1rem',
              opacity: 0.85
            }}
          >
            <div style={{ fontSize: '1.5rem', marginTop: '0.25rem' }}>⭐</div>
            <div>
              <h3 style={{ margin: '0 0 0.25rem 0', fontSize: '1.125rem', color: 'var(--color-text-primary)' }}>
                Ôn tập SET0 Cũ (60 câu)
              </h3>
              <p style={{ margin: 0, color: 'var(--color-text-secondary)', fontSize: '0.875rem', lineHeight: '1.4' }}>
                Gồm 60 câu hỏi lọc từ set 0 cũ để ôn tập tập trung.
              </p>
            </div>
          </div>

          {/* Exam Original */}
          <div 
            onClick={() => setSelectedMode("exam")}
            style={{
              padding: '1.25rem 1.5rem',
              borderRadius: 'var(--radius-lg)',
              border: selectedMode === "exam" ? '2px solid var(--color-brand-cyan)' : '1px solid var(--color-border)',
              backgroundColor: selectedMode === "exam" ? 'rgba(6, 182, 212, 0.05)' : 'var(--color-bg-surface)',
              cursor: 'pointer',
              transition: 'all 0.2s',
              display: 'flex',
              alignItems: 'flex-start',
              gap: '1rem',
              opacity: 0.85
            }}
          >
            <div style={{ fontSize: '1.5rem', marginTop: '0.25rem' }}>📝</div>
            <div>
              <h3 style={{ margin: '0 0 0.25rem 0', fontSize: '1.125rem', color: 'var(--color-text-primary)' }}>
                Thi thử Bộ đề cũ (65 câu)
              </h3>
              <p style={{ margin: 0, color: 'var(--color-text-secondary)', fontSize: '0.875rem', lineHeight: '1.4' }}>
                Đề thi 65 câu trích xuất ngẫu nhiên từ kho đề 272 câu cũ.
              </p>
            </div>
          </div>
        </div>
      </div>

      <div style={{ display: 'flex', justifyContent: 'center', marginTop: '2rem' }}>
        <Link 
          href={getHref()} 
          className="btn-primary" 
          style={{ 
            textDecoration: 'none', 
            display: 'flex', 
            alignItems: 'center', 
            justifyContent: 'center', 
            gap: '0.5rem',
            backgroundColor: 'var(--color-brand-cyan)',
            color: 'white',
            padding: '0.875rem 3rem',
            borderRadius: 'var(--radius-lg)',
            fontSize: '1.125rem',
            fontWeight: '600',
            width: '100%',
            boxShadow: '0 4px 15px rgba(6, 182, 212, 0.25)',
            transition: 'all 0.2s'
          }}
          onMouseOver={(e) => {
            e.currentTarget.style.transform = 'translateY(-2px)';
            e.currentTarget.style.boxShadow = '0 6px 20px rgba(6, 182, 212, 0.35)';
          }}
          onMouseOut={(e) => {
            e.currentTarget.style.transform = 'none';
            e.currentTarget.style.boxShadow = '0 4px 15px rgba(6, 182, 212, 0.25)';
          }}
        >
          {getButtonText()} <ArrowRight size={20} />
        </Link>
      </div>
    </main>
  );
}
