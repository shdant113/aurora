run:
	python3 -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload

run-deploy:
	python3 -m uvicorn app:app --reload