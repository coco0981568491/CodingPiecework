import numpy as np
import pandas as pd
from io import BytesIO
from io import StringIO

def generateLease(excel_file, lease_template):

    # read the content of excel and replace the corresponding texts in the contract_template word doc.
    content = pd.read_excel(excel_file)


    # output = StringIO()
    # output.write(content_altered)
    
    # return output