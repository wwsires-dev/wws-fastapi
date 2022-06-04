FROM python:3.10-bullseye

SHELL ["/bin/bash", "-c"]

ENV PATH="/home/wws/.local/bin:/opt/mssql-tools18/bin:${PATH}"
ENV ACCEPT_EULA=Y

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

RUN apt-get -y update
RUN apt-get install -y msodbcsql18
RUN apt-get install -y mssql-tools18
RUN apt-get install -y unixodbc-dev

RUN useradd -ms /bin/bash wws
USER wws
WORKDIR /home/wws

COPY ./app /home/wws/app
COPY ./pyproject.toml /home/wws
COPY ./pdm.lock /home/wws

RUN python -m pip install --upgrade pip

RUN pip install --user pdm

RUN pdm --pep582 >> /home/wws/.bash_profile

RUN pdm install

EXPOSE 80

CMD pdm run uvicorn app.main:app --host=0.0.0.0 --port=80


