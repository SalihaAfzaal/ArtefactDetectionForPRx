

**Artefact Detection for PRx**


Welcome to a small project of my bachelor's thesis, which is aimed at detecting a simple artefact, removing it and then filling the missing parts with three different interpolation
methods. 

**Installation**

**1. Clone the repository to your local machine:**

    git clone https://github.com/SalihaAfzaal/ArtefactDetectionForPRx.git

**2. Navigate to the project directory:**


    _cd ArtefactDetectionForPRx_



**3. (Optional) Create a virtual environment to isolate project dependencies:**

    _python -m venv venv_

**4. Activate the virtual environment:**
**Windows:**

    venv\Scripts\activate

**Linux/Mac:**

    source venv/bin/activate

**5. Install the required dependencies:**

    pip install -r requirements.txt

**6.Run the setup script to install the project:**

    python setup.py install

**7. Usage**

After installing the project, you can import the relevant modules and functions into your Python scripts:
   
    from data.generate_data import generate_data

_Example usage
 
      icp, abp = generate_data()_






