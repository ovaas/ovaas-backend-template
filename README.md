# ovaas-backend-template

## Prerequisites
- Windows 10
- Visual Studio Code
- Docker for Windows
- Node.js (npm)
- Azure Storage Explorer

## Setup Development Environment

### Install softwares described as prerequisites
Recommend to install latest version of each software.

### Install Azure Functions Core Tools
- Download windows installer [here](https://docs.microsoft.com/ja-jp/azure/azure-functions/functions-run-local?tabs=windows%2Ccsharp%2Cbash#install-the-azure-functions-core-tools) and install it.
    - v3.x is recommended.

### Install VSCode Extensions
- Launch VSCode
- Go to the Extention pane
- Search and install the extentions below
    - Azure Functions
    - REST Client

### Clone this repository
- Launch command prompt
- Clone this repository by the command below
    ```cmd
    git clone 
    ```
- Launch VSCode by the command below
    ```cmd
    cd REPOSITORY_ROOT_DIR
    code .
    ```
### Create Python venv on VSCode
It should be created automatically by VSCode when it launchs but you can create it by yourselves using the instructions below if it is not created.

- Launch command prompt in VSCode
- Create venv by the command below
    This command will create a venv named ".venv" 
    ```cmd
    python -m venv .venv
    ```
- Choose Python interpreter 
Launch "Command Palette" and type "Python: Select Interpreter", then you can choose a python interpreter in the venv youjust created.

### Launch a local Azure Storage as a Docker container
Now you are ready to launch some docker containers for developping. The first one is a local Azure Storage. Do it following the command below.
- Launch a local Azure storage using the Azurite Docker image
    ```cmd
    scripts\LaunchAzurite.bat
    ```
    After the command executed, check if local Azure storage is launched by Azure Storage Explorer.

### Launch a local OpenVINO Model server with a pre-trained model
- Look at the list of all pre-trained models by the command below.
    ```cmd
    scripts\GetModelList.bat
    ```
- Choose one model to download and download it by the command below. The name "human-pose-estimation-0001" can be changed as you need.
    ```cmd
    scripts\DownloadModel.bat human-pose-estimation-0001
    ```
- Check if the model is downloaded in local folder. For example, above "human-pose-estimation-0001" should be here.
    ```cmd
    REPOSITORY_ROOT_DIR/models/intel/human-pose-estimation-0001/FPXX
    ```
- Copy the absolute path to the XML file and the BIN file of the pre-trained model and upload the model to the local Azure Storage by the command below.
    ```cmd
    python scripts\UploadModelFilesToAzureStorage.py --model_name human-pose-estimation --xml_file_path REPOSITORY_ROOT_DIR/models/intel/human-pose-estimation-0001/FPXX\human-pose-estimation-0001.xml --bin_file_path REPOSITORY_ROOT_DIR/models/intel/human-pose-estimation-0001/FPXX\human-pose-estimation-0001.bin --connection_string "AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;DefaultEndpointsProtocol=http;BlobEndpoint=http://127.0.0.1:10000/devstoreaccount1;"
    ```
    Here you need four parameters.
    
    - --model_name: The unique model name
    - --xml_file_path: The absolute path to the XML file of the pre-trained model
    - --bin_file_path: The absolute path to the BIN file of the pre-trained model
    - --connection_string: The connection string to access the local Azure Storage. You can get this on Azure Storage explorer but probably above sample string will also work fine for your environment.
- Launch a local OpenVINO model server
    ```cmd
    scripts\LaunchOVMS.bat human-pose-estimation 192.168.10.107
    ```
    Here you need two parameters.

    - First parameter: The unique model name you just named when to upload the model to the local Azure storage.
    - Secon Parameter: Your PC's IP address to access the internet. The "localhost" and "127.0.0.1" will not work fine.

### Launch an Azure functions emulater on VSCode
- From the "Run" on the menu bar, click "Start Debugging". Then the emulater should start automatically. You will see the logs like below if it starts successfully.
    ```cmd
    Azure Functions Core Tools
    Core Tools Version:       3.0.3442 Commit hash: 6bfab24b2743f8421475d996402c398d2fe4a9e0  (64-bit)
    Function Runtime Version: 3.0.15417.0


    Functions:

            HttpTriggerHumanPose: [GET,POST] http://localhost:7071/api/HttpTriggerHumanPose

    For detailed output, run func with --verbose flag.
    [2021-05-10T02:00:03.532Z] Worker process started and initialized.
    [2021-05-10T02:00:03.721Z] Host lock lease acquired by instance ID '000000000000000000000000F6FB3AFD'.
    ```
### Run the sample application
- Open the file called "request.http".
- Click the "Send Request" on the top of the pane, then you can see the inference result on the other pane opened like this.
![Sample Inference Result](img/result.png "sample result")

## Develop your custom application

### 