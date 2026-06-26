# TODO - Royal Enfield AI Diagnostic Assistant

## Completed
- [x] Inspect current project structure and confirm which artifacts are safe to remove
- [x] Remove persisted vector store directory (vector_db)
- [x] Remove persisted SQLite chat DB (data/royal_enfield.db) to restart clean
- [x] Update README with complete setup and usage instructions
- [x] Add requirements.txt with all dependencies

## In Progress
- [ ] Wire Chroma ingestion/retrieval for embedding-based retrieval
- [ ] Test full backend-frontend integration

## Pending
- [ ] Quick manual test: POST /chat and GET /history after restart
- [ ] Performance optimization for large datasets
- [ ] Add error handling and validation
- [ ] Deploy to production environment
