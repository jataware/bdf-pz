FROM node:20 AS nodebuilder

COPY ./custom-ui /custom-ui
WORKDIR /custom-ui
RUN npm ci && npm run build


FROM python:3.11.5
RUN useradd -m jupyter
EXPOSE 8888

RUN apt update && apt install -y lsof

# Install Python requirements
RUN pip install --upgrade --no-cache-dir hatch pip

COPY --chown=1000:1000 . /jupyter/
RUN chown -R 1000:1000 /jupyter
RUN pip install --no-build-isolation beaker-kernel~=1.8.8

RUN pip install --no-build-isolation cloudpickle cython editables
RUN pip install --no-build-isolation git+https://github.com/mitdbg/palimpzest.git@6ab5b5bcfdc36b3b51d136b41ab8ce95d7cd5005
RUN python -c "import palimpzest"
RUN pip install --no-build-isolation -e /jupyter

RUN rm -r /usr/local/lib/python3.11/site-packages/beaker_kernel/server/ui/*
COPY --from=nodebuilder /custom-ui/dist/ /usr/local/lib/python3.11/site-packages/beaker_kernel/server/ui/

# Switch to non-root user. It is crucial for security reasons to not run jupyter as root user!
USER jupyter
WORKDIR /jupyter


# Service
CMD ["python", "-m", "beaker_kernel.server.main", "--ip", "0.0.0.0"]
