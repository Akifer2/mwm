# 1. criar e ativar o ambiente
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\Activate

# 2. instalar dependências
pip install -r requirements.txt

# 3. configurar variáveis em .env
echo "DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/workshop_db" >> .env
echo "ALLOWED_ORIGINS=http://localhost:3000" >> .env

# 4. inicializar Alembic
alembic init database/migrations
alembic revision --autogenerate -m "create vehicles"
alembic upgrade head

# 5. popular dados de exemplo
python database/seed.py

# 6. subir a API (hot-reload)
uvicorn app.main:app --reload
