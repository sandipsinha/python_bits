import unittest
from dbtableexport import export_db_table, run_export_script
from mock import patch, Mock,MagicMock
import dbtableexport  as dbexp
TNAME = 'mockfile'
NOTVALID = '@1212& '
DELIM = ','

fileobject = '/Users/ssinha/pythonplay/mockfile.sql'

def getTestFile():
    thefile = open(fileobject,'r')
    return thefile

class FilexportTest(unittest.TestCase):
    @patch.object(dbexp, 'create_file')
    @patch.object(dbexp,'run_export_script')
    def test_file_count(self, mock_export, mock_file):
        mock_export.return_value = True
        mock_file.return_value = getTestFile()
        count = dbexp.export_db_table(TNAME, DELIM)
        self.assertEqual(count,4)

    @patch.object(dbexp,'run_export_script')
    def test_invalid(self, mock_export):
        mock_export.return_value = True
        count = dbexp.export_db_table(NOTVALID, DELIM)
        self.assertEqual(count,0)

if __name__ == '__main__':
    unittest.main()
        
