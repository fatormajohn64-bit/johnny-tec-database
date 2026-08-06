-- Seed data for the developers table.
-- INSERT OR IGNORE + the UNIQUE constraint on username means this is safe
-- to run every deploy/startup without creating duplicate rows.

INSERT OR IGNORE INTO developers (name, username, role, bio, github_url, primary_stack)
VALUES
(
    'John Fatoma',
    'johnny-tec-dev',
    'Founder & Lead Developer',
    'Creator of Johnny Tec AI ecosystem.',
    'https://github.com/johnny-tec-dev',
    'Python, SQL, AI Architectures'
),
(
    'Invisible 911',
    'invisible-911',
    'Developer Alias',
    'Secondary developer profile and system alias.',
    'https://github.com/invisible-911',
    'Database Engineering & Security'
);
