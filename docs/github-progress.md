# GitHub Progress Sync

Progress sync uses a private GitHub Gist as a tiny free remote save file.

## Setup

1. Create a private Gist with one file named `pd1-progress.json`.
2. Put this initial content in the file:

```json
{
  "study": {}
}
```

3. Create a GitHub token that can read and write Gists.
4. Add these environment variables locally and on Vercel:

```env
GITHUB_TOKEN=github_pat_or_fine_grained_token
GITHUB_GIST_ID=your_private_gist_id
GITHUB_GIST_FILE_NAME=pd1-progress.json
PROGRESS_KEY=choose-a-small-personal-secret
NEXT_PUBLIC_PROGRESS_KEY=choose-a-small-personal-secret
```

`GITHUB_TOKEN` stays server-side. `NEXT_PUBLIC_PROGRESS_KEY` is only a lightweight guard for a personal app, so keep the Gist private and do not reuse that value anywhere important.

If the GitHub variables are missing or GitHub is unavailable, study progress still saves to `localStorage`.
