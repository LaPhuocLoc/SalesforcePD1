import React from 'react';

interface FormattedTextProps {
  text: string;
  isOption?: boolean;
}

export default function FormattedText({ text, isOption }: FormattedTextProps) {
  if (!text) return null;

  if (isOption) {
    // For options, we fix merged lines but keep it as simple wrapping text
    const processedText = text
      .replace(/;\s+(?=(String|Integer|Boolean|Id|Account|Contact|Opportunity|Lead|List|Set|Map|try|catch|if|else|for|while|update|insert|delete|upsert|System\.|Database\.|return|public|private|global)\b)/g, ';\n')
      .replace(/\{\s+(?=(String|Integer|Boolean|Id|Account|Contact|Opportunity|Lead|List|Set|Map|try|catch|if|else|for|while|update|insert|delete|upsert|System\.|Database\.|return|public|private|global)\b)/g, '{\n')
      .replace(/\}\s+(?=(catch|else|finally|public|private|global)\b)/g, '}\n');
    
    return <div style={{ whiteSpace: 'pre-wrap', wordBreak: 'break-word' }}>{processedText}</div>;
  }

  const lines = text.split('\n');
  const blocks: { type: 'text' | 'code'; lines: string[] }[] = [];
  let currentBlock: { type: 'text' | 'code'; lines: string[] } = { type: 'text', lines: [] };

  const isCodeLine = (line: string) => {
    const t = line.trim();
    if (!t) return false;
    if (t.endsWith(';') || t.endsWith('{') || t === '}') return true;
    if (t.startsWith('for(') || t.startsWith('for (') || t.startsWith('if(') || t.startsWith('if ') || t.startsWith('else {') || t.startsWith('else{')) return true;
    if (t.startsWith('trigger ') || t.startsWith('public ') || t.startsWith('private ') || t.startsWith('global ') || t.startsWith('class ')) return true;
    if (t.match(/^[A-Z][a-zA-Z0-9_]*(<.+>)?\s+[a-zA-Z0-9_]+\s*(=|;)/)) return true; // e.g. "String name =" or "List<Id> ids;"
    if (t.includes('System.debug') || t.includes('Database.')) return true;
    if (t.startsWith('SELECT ') || t.startsWith('FROM ') || t.startsWith('WHERE ') || t.includes('[SELECT ')) return true;
    return false;
  };

  lines.forEach((line) => {
    // PDF artifacts cleanup
    let cleanLine = line.replace(/0\{$/, ') {').replace(/\}\{$/, ') {');
    
    if (isCodeLine(cleanLine)) {
      // Split multiple statements on the same line if they are separated by semicolon + space + Keyword
      // This fixes PDF parsing where multiple lines were merged into one.
      const splitRegex = /;\s+(?=(String|Integer|Boolean|Id|Account|Contact|Opportunity|Lead|List|Set|Map|try|catch|if|else|for|while|update|insert|delete|upsert|System\.|Database\.|return|public|private|global)\b)/g;
      const braceRegex = /\{\s+(?=(String|Integer|Boolean|Id|Account|Contact|Opportunity|Lead|List|Set|Map|try|catch|if|else|for|while|update|insert|delete|upsert|System\.|Database\.|return|public|private|global)\b)/g;
      const closeBraceRegex = /\}\s+(?=(catch|else|finally|public|private|global)\b)/g;

      const splitLines = cleanLine
        .replace(splitRegex, ';\n')
        .replace(braceRegex, '{\n')
        .replace(closeBraceRegex, '}\n')
        .split('\n');

      if (currentBlock.type === 'text') {
        if (currentBlock.lines.length > 0) blocks.push(currentBlock);
        currentBlock = { type: 'code', lines: [] };
      }
      currentBlock.lines.push(...splitLines);
    } else {
      // If it's a short line or empty line inside a code block, keep it as code to prevent fragmentation
      if (currentBlock.type === 'code' && (cleanLine.trim() === '' || cleanLine.length < 15 || cleanLine.startsWith('//'))) {
        currentBlock.lines.push(cleanLine);
      } else {
        if (currentBlock.type === 'code') {
          if (currentBlock.lines.length > 0) blocks.push(currentBlock);
          currentBlock = { type: 'text', lines: [] };
        }
        currentBlock.lines.push(cleanLine);
      }
    }
  });

  if (currentBlock.lines.length > 0) blocks.push(currentBlock);

  return (
    <div className="formatted-text">
      {blocks.map((block, i) => {
        if (block.type === 'text') {
          return (
            <p key={i} className="text-block">
              {block.lines.join('\n')}
            </p>
          );
        } else {
          // Auto-indent
          let indentLevel = 0;
          const formattedCode = block.lines
            .map((line) => {
              let trimmed = line.trim();
              if (trimmed.startsWith('}')) {
                indentLevel = Math.max(0, indentLevel - 1);
              }

              const indented = '  '.repeat(indentLevel) + trimmed;

              if (trimmed.endsWith('{') || (trimmed.includes('{') && !trimmed.includes('}'))) {
                indentLevel++;
              }
              return indented;
            })
            .join('\n');

          return (
            <pre key={i} className="code-block">
              <code>{formattedCode}</code>
            </pre>
          );
        }
      })}
    </div>
  );
}
