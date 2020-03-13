# From https://github.com/microsoft/AzureML-BERT/blob/master/finetune/PyTorch/dockerfile

FROM mcr.microsoft.com/azureml/base:openmpi3.1.2-ubuntu18.04

RUN apt update && apt install git -y && rm -rf /var/lib/apt/lists/* && apt-get update

# Install dotnet sdk Linux distribution
# From https://docs.microsoft.com/en-us/dotnet/core/install/linux-package-manager-ubuntu-1804
RUN apt-get install -y software-properties-common
RUN wget -q https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
RUN dpkg -i packages-microsoft-prod.deb
RUN add-apt-repository universe
RUN apt-get update
RUN apt-get install apt-transport-https
RUN apt-get update
RUN apt-get install -y dotnet-sdk-2.2

# Install ML.NET CLI
# from https://docs.microsoft.com/en-us/dotnet/machine-learning/how-to-guides/install-ml-net-cli
RUN dotnet tool install -g mlnet

# doesn't get added to path
ENV PATH="${PATH}:/root/.dotnet/tools"
