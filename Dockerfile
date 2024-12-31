FROM python:3.11.5
RUN useradd -m jupyter
EXPOSE 8888

RUN apt update && apt install -y lsof

# Install Python requirements
RUN pip install --upgrade --no-cache-dir hatch pip

COPY beaker_kernel-1.8.7b1-py3-none-any.whl /jupyter/
COPY --chown=1000:1000 . /jupyter/
RUN chown -R 1000:1000 /jupyter
RUN pip uninstall beaker_kernel -y
RUN pip install --no-build-isolation /jupyter/beaker_kernel-1.8.7b1-py3-none-any.whl

RUN pip install --no-build-isolation cloudpickle
RUN pip install --no-build-isolation git+https://github.com/mitdbg/palimpzest.git@main
RUN python -c "import palimpzest"
RUN pip install --no-build-isolation -e /jupyter

# Switch to non-root user. It is crucial for security reasons to not run jupyter as root user!
USER jupyter
WORKDIR /jupyter


# Service
CMD ["python", "-m", "beaker_kernel.server.main", "--ip", "0.0.0.0"]
