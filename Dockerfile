FROM python:3
copy . /my_own_dir
WORKDIR /my_own_dir
RUN pip install -r requirements.txt
CMD ["python","mywebsite.py"]