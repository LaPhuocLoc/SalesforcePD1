export const dynamic = "force-dynamic";

type ProgressData = {
  study?: Record<
    string,
    {
      currentIndex: number;
      answered: Record<string, "correct" | "incorrect" | boolean>;
      updatedAt: string;
    }
  >;
};

const gistFileName = process.env.GITHUB_GIST_FILE_NAME || "pd1-progress.json";

function getGitHubConfig() {
  return {
    token: process.env.GITHUB_TOKEN,
    gistId: process.env.GITHUB_GIST_ID,
    progressKey: process.env.PROGRESS_KEY,
  };
}

function emptyProgress(): ProgressData {
  return { study: {} };
}

function json(data: unknown, init?: ResponseInit) {
  return Response.json(data, init);
}

function isAuthorized(request: Request) {
  const { progressKey } = getGitHubConfig();
  if (!progressKey) return true;
  return request.headers.get("x-progress-key") === progressKey;
}

function githubHeaders(token: string) {
  return {
    Accept: "application/vnd.github+json",
    Authorization: `Bearer ${token}`,
    "Content-Type": "application/json",
    "X-GitHub-Api-Version": "2022-11-28",
  };
}

function parseProgress(content: string | undefined): ProgressData {
  if (!content?.trim()) return emptyProgress();

  const parsed = JSON.parse(content) as unknown;
  if (!parsed || typeof parsed !== "object") return emptyProgress();

  return parsed as ProgressData;
}

async function readGistProgress(token: string, gistId: string) {
  const response = await fetch(`https://api.github.com/gists/${gistId}`, {
    cache: "no-store",
    headers: githubHeaders(token),
  });

  if (!response.ok) {
    return {
      ok: false as const,
      status: response.status,
      progress: emptyProgress(),
    };
  }

  const gist = (await response.json()) as {
    files?: Record<string, { content?: string }>;
  };

  return {
    ok: true as const,
    progress: parseProgress(gist.files?.[gistFileName]?.content),
  };
}

export async function GET(request: Request) {
  const { token, gistId } = getGitHubConfig();

  if (!isAuthorized(request)) {
    return json({ error: "Unauthorized" }, { status: 401 });
  }

  if (!token || !gistId) {
    return json({ configured: false, progress: emptyProgress() });
  }

  try {
    const result = await readGistProgress(token, gistId);
    if (!result.ok) {
      return json(
        { configured: true, error: "Unable to read GitHub Gist", progress: result.progress },
        { status: result.status }
      );
    }

    return json({ configured: true, progress: result.progress });
  } catch {
    return json(
      { configured: true, error: "Unable to parse GitHub Gist progress", progress: emptyProgress() },
      { status: 500 }
    );
  }
}

export async function POST(request: Request) {
  const { token, gistId } = getGitHubConfig();

  if (!isAuthorized(request)) {
    return json({ error: "Unauthorized" }, { status: 401 });
  }

  if (!token || !gistId) {
    return json({ configured: false, saved: false });
  }

  let progress: ProgressData;
  try {
    const body = (await request.json()) as { progress?: ProgressData };
    progress = body.progress || emptyProgress();
  } catch {
    return json({ error: "Invalid JSON body" }, { status: 400 });
  }

  const response = await fetch(`https://api.github.com/gists/${gistId}`, {
    method: "PATCH",
    headers: githubHeaders(token),
    body: JSON.stringify({
      files: {
        [gistFileName]: {
          content: `${JSON.stringify(progress, null, 2)}\n`,
        },
      },
    }),
  });

  if (!response.ok) {
    return json(
      { configured: true, saved: false, error: "Unable to write GitHub Gist" },
      { status: response.status }
    );
  }

  return json({ configured: true, saved: true });
}
