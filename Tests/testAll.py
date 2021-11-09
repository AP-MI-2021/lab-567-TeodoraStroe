from Tests.testCRUD import testAdaugaRezervare, testStergeRezervare, testModificaRezervare
from Tests.testDomain import testRezervare
from Tests.testeFunctionalitati import testIeftinire, testClasaSuperioara, testPretMaxim, testOrdonareDupaPret, testSumaPretPeNume
from Tests.testUndo_Redo import test_undo_redo_OrdonareDupaPret, test_undo_redo_ieftinire, test_undo_redo_clasa_superioara, test_undo_redo

def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergeRezervare()
    testModificaRezervare()
    testIeftinire()
    testClasaSuperioara()
    testPretMaxim()
    testOrdonareDupaPret()
    testSumaPretPeNume()
    test_undo_redo_OrdonareDupaPret()
    test_undo_redo_ieftinire()
    test_undo_redo_clasa_superioara()
    test_undo_redo()
