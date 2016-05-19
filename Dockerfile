FROM debian:jessie

# Setup build environment
RUN apt-get update && apt-get install -y \
  build-essential \
  libxml2-dev \
  wget \
&& rm -rf /var/lib/apt/lists/*

# Switch to user-space
ENV HOME /home/tet

# Grab python environment via anaconda
WORKDIR /home/tet
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
RUN bash miniconda.sh -b -p $HOME/miniconda
ENV PATH $HOME/miniconda/bin:$PATH
RUN hash -r
RUN conda config --set always_yes yes --set changeps1 no
RUN conda update -q conda
RUN conda info -a
RUN conda install numpy pytest 
RUN pip install python-igraph 

# Pull in the sources
WORKDIR /home/tet/packtets
ADD setup.py requirements.txt /home/tet/packtets/
ADD packtets /home/tet/packtets/packtets/
RUN ls /home/tet/packtets/
RUN which python3
RUN python3 ./setup.py install

# Run some tests
ENTRYPOINT ["py.test", "-v", "packtets"] 
