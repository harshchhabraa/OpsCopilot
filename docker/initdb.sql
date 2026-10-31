CREATE DATABASE opscopilot_test;

\connect opscopilot
CREATE EXTENSION IF NOT EXISTS vector;

\connect opscopilot_test
CREATE EXTENSION IF NOT EXISTS vector;
