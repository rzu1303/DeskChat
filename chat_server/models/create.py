INIT_DB_QUERY = """
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS public.chat_server_messages (
    id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(64),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
"""
