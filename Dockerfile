FROM python:3.11.5
RUN useradd -m jupyter
RUN useradd -m user
EXPOSE 8888

RUN apt update && apt install -y lsof

# Install Python requirements
RUN pip install --upgrade --no-cache-dir hatch pip

COPY --chown=1000:1000 . /jupyter/
RUN chown -R 1000:1000 /jupyter
RUN pip install --no-build-isolation /jupyter/beaker_kernel-1.9.0a1-py3-none-any.whl

RUN pip install --no-build-isolation cloudpickle cython editables
RUN pip install --no-build-isolation git+https://github.com/mitdbg/palimpzest.git@main
RUN python -c "import palimpzest"
RUN pip install --no-build-isolation -e /jupyter

USER root
RUN mkdir -m 777 /var/run/beaker

WORKDIR /jupyter

# Set default server env variables
ENV BEAKER_AGENT_USER=jupyter
ENV BEAKER_SUBKERNEL_USER=user
ENV BEAKER_RUN_PATH=/var/run/beaker
ENV BEAKER_APP=bdf_pz.app.PalimpzestApp

#ENV CONFIG_TYPE=session


# Service
CMD ["python", "-m", "beaker_kernel.service.server", "--ip", "0.0.0.0"]
