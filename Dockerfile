FROM python:3.11.5
RUN useradd -m jupyter
RUN useradd -m user
EXPOSE 8888

# Setup environment
RUN apt update && apt install -y lsof

# Install Python requirements
RUN pip install --upgrade --no-cache-dir hatch pip
RUN pip install palimpzest 
RUN pip install --no-build-isolation beaker-kernel
RUN pip install cython
RUN pip install editables
# Copy local package to image and install
COPY --chown=1000:1000 . /jupyter/
RUN chown -R 1000:1000 /jupyter
RUN pip install --no-build-isolation -e /jupyter

# Set up for running beaker server
USER root
RUN mkdir -m 777 /var/run/beaker
WORKDIR /jupyter

# Set default server env variables
ENV BEAKER_AGENT_USER=jupyter
ENV BEAKER_SUBKERNEL_USER=user
ENV BEAKER_RUN_PATH=/var/run/beaker
ENV BEAKER_APP=bdf_pz.app.PalimpzestApp

# Service
CMD ["python", "-m", "beaker_kernel.service.server", "--IdentityProvider.token=''"]
