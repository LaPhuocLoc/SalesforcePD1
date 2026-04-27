import React from "react";
import FormattedText from "./FormattedText";

interface Option {
  key: string;
  text: string;
}

interface Question {
  id: number;
  question: string;
  options: Option[];
  correct: string[];
  type: string;
}

interface ExamQuestionCardProps {
  question: Question;
  selectedKeys: string[];
  onChange: (keys: string[]) => void;
}

export default function ExamQuestionCard({
  question,
  selectedKeys,
  onChange
}: ExamQuestionCardProps) {

  const handleOptionClick = (key: string) => {
    if (question.type === "single") {
      onChange([key]);
    } else {
      if (selectedKeys.includes(key)) {
        onChange(selectedKeys.filter((k) => k !== key));
      } else {
        onChange([...selectedKeys, key]);
      }
    }
  };

  const getOptionClass = (key: string) => {
    let classes = "option-button";
    if (selectedKeys.includes(key)) classes += " selected";
    return classes;
  };

  return (
    <div className="study-card-container">
      <div className="study-card-face" style={{ minHeight: 'auto', paddingBottom: '2rem' }}>
        <div className="question-header" style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem' }}>
          <span style={{ color: 'var(--color-brand-cyan)', fontWeight: '600' }}>Câu hỏi #{question.id}</span>
          <span style={{ color: 'var(--color-text-tertiary)', fontSize: '0.875rem' }}>
            {question.type === 'single' ? 'Chọn 1 đáp án' : `Chọn ${question.correct.length} đáp án`}
          </span>
        </div>
        
        <div className="question-text">
          <FormattedText text={question.question} />
        </div>

        <div className="options-list">
          {question.options.map((option) => (
            <button
              key={option.key}
              className={getOptionClass(option.key)}
              onClick={() => handleOptionClick(option.key)}
            >
              <span className="option-key">{option.key}</span>
              <span className="option-text">
                <FormattedText text={option.text} isOption={true} />
              </span>
            </button>
          ))}
        </div>
      </div>
    </div>
  );
}
