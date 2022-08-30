from pages import *
from PyQt5.QtWidgets import QMainWindow,QApplication, QFileDialog
import sys
import os
from ecies.utils import generate_eth_key
from ecies import encrypt, decrypt
import hashlib
from datetime import datetime
import shutil
import pickle
from time import sleep 


class Main_window():
        def __init__(self):
                self.main_win = QMainWindow()
                self.ui = Ui_MainWindow()
                self.folder_name = None
                self.file_name = None
                self.previous_page = None
                self.hashed_files = {} # {h1:[f1h1, f2h1], h2:[f1h2]}
                self.ui.setupUi(self.main_win)
                self.ui.stackedWidget.setCurrentWidget(self.ui.start_page)

                # >>>>>>>> functions connect with buttons <<<<<<<<

                self.ui.duplicates_rem_button.clicked.connect(self.show_folder_page)
                self.ui.files_encrypt_button.clicked.connect(self.show_file_page)
                self.ui.find_button.clicked.connect(self.show_find_duplicates_page)
                self.ui.isolate_button.clicked.connect(self.isolate_duplicates)
                self.ui.delete_button.clicked.connect(self.delete_duplicates)
                self.ui.stats_button.clicked.connect(self.show_stats_page)
                self.ui.encrypt_button.clicked.connect(self.encrypt_files)
                self.ui.decrypt_button.clicked.connect(self.decrypt_files)
                self.ui.folder_browse_button.clicked.connect(self.browse_folder)
                self.ui.file_brwose_button.clicked.connect(self.browse_file)
                # >>>>>>>> functions connect with buttons end <<<<<<<<

                # >>>>>>>> Back Buttons connect <<<<<<<<

                self.ui.folder_back_button.clicked.connect(self.back_connect)
                self.ui.file_back_button.clicked.connect(self.back_connect)
                self.ui.dup_back_button.clicked.connect(self.back_connect)
                self.ui.stats_back_button.clicked.connect(self.back_connect)
                # >>>>>>>> Back Buttons connect end <<<<<<<<

                # >>>>>>>> keys generation <<<<<<<<

                if os.path.exists("HERO_PRIV_KEY_HEX.key"):

                        with open("HERO_PRIV_KEY_HEX.key",'rb') as f:
                                self.privKeyHex = pickle.load(f)
                        
                else:
                        self.privKey = generate_eth_key()
                        self.privKeyHex = self.privKey.to_hex()

                        with open("HERO_PRIV_KEY_HEX.key",'wb') as f:
                                pickle.dump(self.privKeyHex, f, protocol=pickle.HIGHEST_PROTOCOL)

                #public key generation
                
                if os.path.exists("HERO_PUB_KEY_HEX.key"):
    
                        with open("HERO_PUB_KEY_HEX.key",'rb') as f:
                                self.pubKeyHex = pickle.load(f)
                        
                else:
                        self.pubKeyHex = self.privKey.public_key.to_hex()

                        with open("HERO_PUB_KEY_HEX.key",'wb') as f:
                                pickle.dump(self.pubKeyHex, f, protocol=pickle.HIGHEST_PROTOCOL)
                                

                self.hasher = hashlib.sha256()
                # >>>>>>>> keys generation end <<<<<<<<

                
        # connect back buttons functionality
        def back_connect(self):
                if self.previous_page == "start_page":
                        self.ui.stackedWidget.setCurrentWidget(self.ui.start_page)
                if self.previous_page == "folder_select_page":
                        self.previous_page = "start_page"
                        self.ui.stackedWidget.setCurrentWidget(self.ui.folder_select_page)
                elif self.previous_page == "duplicates_page":
                        self.previous_page = "folder_select_page"
                        self.ui.stackedWidget.setCurrentWidget(self.ui.duplicates_page)

                
        # open browse folders for duplication removing
        def browse_folder(self):
                self.folder_name = str(QFileDialog.getExistingDirectory())
                self.ui.folder_browser_box.setText(self.folder_name)

        # open browse folders for duplication removing
        def browse_file(self):
                self.file_name = QtWidgets.QFileDialog.getOpenFileName()
                self.file_name = self.file_name[0]
                self.ui.file_browser_box.setText(self.file_name)

        
        def show_folder_page(self):
                self.previous_page = "start_page"
                self.ui.stackedWidget.setCurrentWidget(self.ui.folder_select_page)

        def show_file_page(self):
                self.previous_page = "start_page"
                self.ui.stackedWidget.setCurrentWidget(self.ui.file_select_page)
        

        # def read_file(self,path):
        #         with open(path,'r') as f:
        #                 f.read()
                        
        def absoluteFilePaths(self,directory):
                files = []
                for dirpath,_,filenames in os.walk(directory):
                        for f in filenames:
                                files.append( os.path.abspath(os.path.join(dirpath, f)))
                return files

        def isolate_duplicates(self):
                current_date = datetime.now().strftime("%d-%m-%Y")
                duplicates_folder = os.path.join(self.folder_name, 'duplicates '+ current_date)
                duplicated_files = [file for d_files in self.hashed_files.values() for i,file in enumerate(d_files) if i > 0]

                if not os.path.isdir(duplicates_folder):       
                        new_path = os.makedirs(duplicates_folder)
                
                for file in duplicated_files:
                        try:
                                shutil.move(file, duplicates_folder)
                        except: 
                                pass
        
        def delete_duplicates(self):
                duplicated_files = [file for d_files in self.hashed_files.values() for i,file in enumerate(d_files) if i > 0]

                for file in duplicated_files:
                        try:
                                os.remove(file)
                        except:
                                pass
        
        def show_find_duplicates_page(self):

                if self.folder_name == None:
                        self.previous_page = "start_page"
                        self.ui.stackedWidget.setCurrentWidget(self.ui.folder_select_page)
                        
                        error_dialog = QtWidgets.QErrorMessage()
                        error_dialog.showMessage('You did not choose any path!')
                        sleep(3)
                else:
                        
                        self.previous_page = "folder_select_page"
                        self.ui.stackedWidget.setCurrentWidget(self.ui.duplicates_page)

                        tested_files = self.absoluteFilePaths(self.folder_name)
                
                        self.ui.files_num.setText('  '+ str(len(tested_files)))

                        
                        for f in tested_files:
                                with open(f,'rb') as file:
                                        file_bytes = file.read() # read file as bytes
                                        readable_hash = hashlib.md5(file_bytes).hexdigest()

                                        if readable_hash not in self.hashed_files:
                                                self.hashed_files[readable_hash] = [f]
                                        else:
                                                self.hashed_files[readable_hash].append(f)

                


        def show_stats_page(self):
                
                self.previous_page = "duplicates_page"

                recurrent = sum([len(x)-1 for x in self.hashed_files.values()])
                self.ui.num_duplicates.setText(str(recurrent))

                saved_space = sum([os.path.getsize(x[0]) * (len(x)-1) for x in self.hashed_files.values()])
                total_space = sum([os.path.getsize(x[0]) * (len(x)) for x in self.hashed_files.values()])
                saved_percantage = round((saved_space/total_space)*100,2)
                self.ui.removed_size.setText(str(saved_percantage)+"%")

                saved_size_mb = round(float(saved_space) / (1024*1024),2)
                self.ui.saved_size.setText(str(saved_size_mb))

                self.ui.stackedWidget.setCurrentWidget(self.ui.stats_page)


        def encrypt_files(self):

                if self.file_name == None:
                        self.previous_page = "start_page"
                        self.ui.stackedWidget.setCurrentWidget(self.ui.file_select_page)
                else:
                        with open(self.file_name,'rb') as file:
                                file_bytes = file.read()
                                encrypted_file = encrypt(self.pubKeyHex, file_bytes)

                
                        with open(f"{self.file_name}.hero",'wb') as file:
                                file.write(encrypted_file)
                

                
                
                
        
        def decrypt_files(self):
                with open(self.file_name,'rb') as file:
                        encrypted_file = file.read()
                        decrypted_file = decrypt(self.privKeyHex, encrypted_file)

                with open(f"{self.file_name[:-5]}",'wb') as file:
                                file.write(decrypted_file)
                

                
                
        def show(self):
                self.main_win.show() 
      
                

if __name__ == "__main__":
        app = QApplication(sys.argv)
        main_win = Main_window()
        main_win.show()
        sys.exit(app.exec_())

        