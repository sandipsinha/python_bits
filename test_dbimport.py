import unittest
from dbtableexport import export_db_table, run_export_script
from mock import patch, Mock,MagicMock
import dbtableimport  as dbimp
TNAME = 'mockfile'
NOTVALID = '@1212& '
DELIM = ','

fileobject = '/Users/ssinha/pythonplay/mockfile.sql'

def getTestFile():
    thefile = open(fileobject,'r')
    return thefile

class FilimportTest(unittest.TestCase):
    @patch.object(dbimp, 'verify_file')
    @patch.object(dbimp,'run_import_script')
    def test_file_count(self, mock_import, mock_file):
        mock_import.return_value = True
        mock_file.return_value = getTestFile()
        upload_ind = dbimp.import_db_table(TNAME, DELIM)
        self.assertEqual(upload_ind,True)

    @patch.object(dbimp,'run_import_script')
    def test_invalid(self, mock_import):
        mock_import.return_value = True
        upload_ind = dbimp.import_db_table(NOTVALID, DELIM)
        self.assertEqual(upload_ind,False)

    
    @patch.object(dbimp, 'verify_file')
    def test_valid_script(self, mock_file):
        mock_file.return_value = getTestFile()
        import ipdb;ipdb.set_trace()
        upload_ind = dbimp.import_db_table(TNAME, DELIM)
        self.assertEqual(upload_ind,False)

if __name__ == '__main__':
    unittest.main()
        
