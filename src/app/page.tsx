"use client";

import React, { useState } from "react";
import Link from "next/link";
import { BookOpen, PenTool, ArrowRight } from "lucide-react";

export default function HomePage() {
  const [selectedMode, setSelectedMode] = useState<"exam" | "study" | "study_set0">("study");

  return (
    <main className="container" style={{ paddingBottom: '4rem', paddingTop: '4rem', maxWidth: '600px' }}>
      <div style={{ marginBottom: '3rem' }}>
        <h1 style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', fontSize: '2rem', marginBottom: '0.5rem', color: 'var(--color-text-primary)' }}>
          🎓 Platform Developer I (PD1)
        </h1>
        <p style={{ color: 'var(--color-text-secondary)', fontSize: '1.125rem' }}>
          Chọn chế độ luyện thi phù hợp với bạn
        </p>
      </div>

      <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', marginBottom: '2rem' }}>
        <div 
          onClick={() => setSelectedMode("exam")}
          style={{
            padding: '1.5rem',
            borderRadius: 'var(--radius-lg)',
            border: selectedMode === "exam" ? '2px solid var(--color-brand-cyan)' : '1px solid var(--color-border)',
            backgroundColor: selectedMode === "exam" ? 'rgba(6, 182, 212, 0.05)' : 'var(--color-bg-surface)',
            cursor: 'pointer',
            transition: 'all 0.2s',
            display: 'flex',
            alignItems: 'flex-start',
            gap: '1rem'
          }}
        >
          <div style={{ fontSize: '1.5rem' }}>📝</div>
          <div>
            <h3 style={{ margin: '0 0 0.25rem 0', fontSize: '1.125rem', color: 'var(--color-text-primary)' }}>
              Thi thật (65 câu - 105 phút)
            </h3>
            <p style={{ margin: 0, color: 'var(--color-text-secondary)', fontSize: '0.875rem' }}>
              Mô phỏng 100% bài thi thật. Random 65 câu, đếm ngược 105 phút.
            </p>
          </div>
        </div>

        <div 
          onClick={() => setSelectedMode("study")}
          style={{
            padding: '1.5rem',
            borderRadius: 'var(--radius-lg)',
            border: selectedMode === "study" ? '2px solid var(--color-brand-cyan)' : '1px solid var(--color-border)',
            backgroundColor: selectedMode === "study" ? 'rgba(6, 182, 212, 0.05)' : 'var(--color-bg-surface)',
            cursor: 'pointer',
            transition: 'all 0.2s',
            display: 'flex',
            alignItems: 'flex-start',
            gap: '1rem'
          }}
        >
          <div style={{ fontSize: '1.5rem' }}>📖</div>
          <div>
            <h3 style={{ margin: '0 0 0.25rem 0', fontSize: '1.125rem', color: 'var(--color-text-primary)' }}>
              Ôn tập (Tất cả 272 câu)
            </h3>
            <p style={{ margin: 0, color: 'var(--color-text-secondary)', fontSize: '0.875rem' }}>
              Làm toàn bộ 272 câu hỏi. Không giới hạn thời gian, xem đáp án ngay sau mỗi câu.
            </p>
          </div>
        </div>

        <div 
          onClick={() => setSelectedMode("study_set0")}
          style={{
            padding: '1.5rem',
            borderRadius: 'var(--radius-lg)',
            border: selectedMode === "study_set0" ? '2px solid var(--color-brand-cyan)' : '1px solid var(--color-border)',
            backgroundColor: selectedMode === "study_set0" ? 'rgba(6, 182, 212, 0.05)' : 'var(--color-bg-surface)',
            cursor: 'pointer',
            transition: 'all 0.2s',
            display: 'flex',
            alignItems: 'flex-start',
            gap: '1rem'
          }}
        >
          <div style={{ fontSize: '1.5rem' }}>⭐</div>
          <div>
            <h3 style={{ margin: '0 0 0.25rem 0', fontSize: '1.125rem', color: 'var(--color-text-primary)' }}>
              Ôn tập Bộ Đề SET0 (60 câu)
            </h3>
            <p style={{ margin: 0, color: 'var(--color-text-secondary)', fontSize: '0.875rem' }}>
              Ôn tập riêng 60 câu hỏi của Set 0 mới cập nhật.
            </p>
          </div>
        </div>
      </div>

      <div style={{ display: 'flex', gap: '1rem', marginTop: '3rem' }}>
        <button className="btn-secondary" disabled style={{ opacity: 0 }}>
          ← Quay lại
        </button>
        <Link 
          href={selectedMode === "exam" ? "/exam" : selectedMode === "study_set0" ? "/study?set=0" : "/study"} 
          className="btn-primary" 
          style={{ 
            textDecoration: 'none', 
            display: 'flex', 
            alignItems: 'center', 
            justifyContent: 'center', 
            gap: '0.5rem',
            backgroundColor: 'var(--color-brand-cyan)',
            color: 'white',
            padding: '0.75rem 2rem',
            borderRadius: 'var(--radius-md)'
          }}
        >
          Bắt đầu thi <ArrowRight size={18} />
        </Link>
      </div>
    </main>
  );
}
