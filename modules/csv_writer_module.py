from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox

from modules.log_class import logger

import csv
from pathlib import Path

class CSVWriterClass(QObject):
    exportEnd = Signal(bool)
    exportError = Signal(bool)
    
    def __init__(self, parent = None):
        super().__init__(parent)    

        # self.base_path = ""
        
    def export_user_data(self, data):
        if data:
            try:
                csv_path = Path(f"dados_de_uso/paciente_{data["userId"]}_{data["userName"][0][0]}/{data["userHand"]}")#create folder structure
                csv_path.mkdir(parents=True, exist_ok=True)
                raw_data_path = csv_path / "Dados_brutos_por_sessao"
                statistical_data_path = csv_path / "Dados_estatisticos_por_sessao"
                summary_statistical_path = csv_path / "Resumo_dados_estatisticos"
                raw_data_path.mkdir(parents=True, exist_ok=True)
                statistical_data_path.mkdir(parents=True, exist_ok=True)
                summary_statistical_path.mkdir(parents=True, exist_ok=True)
                
                raw_data = [#list to struct
                    {
                        "finger": row[0],
                        "pressure": row[1],
                        "timestamp": row[2]
                    }
                    for row in data["raw_data"]
                ]
                
                raw_csv_file = raw_data_path / f"dados_brutos_{data["sessionDateString"][0][0].replace(':','-')}.csv"#create file for raw data
                with open(raw_csv_file, "w", newline = '') as file:#write on file
                    fieldNames = ["finger","pressure","timestamp"]
                    writer = csv.DictWriter(file, fieldnames=fieldNames)
                    writer.writeheader()
                    writer.writerows(raw_data)

                session_data = [#list to struct
                    {
                        "max_little": row[0][0],
                        "avg_little": row[1][0],
                        "min_little": row[2][0],
                        "total_presses_little": row[3][0],
                        "max_ring": row[0][1],
                        "avg_ring": row[1][1],
                        "min_ring": row[2][1],
                        "total_presses_ring": row[3][1],
                        "max_middle": row[0][2],
                        "avg_middle": row[1][2],
                        "min_middle": row[2][2],
                        "total_presses_middle": row[3][2],
                        "max_index_thumb": row[0][3],
                        "avg_index_thumb": row[1][3],
                        "min_index_thumb": row[2][3],
                        "total_presses_index_thumb": row[3][3],
                    }
                    for row in data["session_data"]
                ]
                session_csv_file = statistical_data_path / f"dados_sessao_{data["sessionDateString"][0][0].replace(':','-')}.csv"#create file for session data
                with open(session_csv_file, "w", newline='') as file:#write session file
                    fieldNames = ["max_little","avg_little","min_little","total_presses_little",
                        "max_ring","avg_ring","min_ring","total_presses_ring",
                        "max_middle","avg_middle","min_middle","total_presses_middle",
                        "max_index_thumb","avg_index_thumb","min_index_thumb","total_presses_index_thumb"]
                    writer = csv.DictWriter(file,fieldNames)
                    writer.writeheader()
                    writer.writerows(session_data)
                    
                #headers - avg_press_finger x 4, timestamp
                
                pressure_data = data["summary_data"][:4]
                logger.debug(f"export_user_data pressure_data:{type(pressure_data[2])}")
                
                avg_press_summary = []

                fingers = ["little", "ring", "middle", "index"]

                avg_press_summary = []

                for i, finger in enumerate(fingers):
                    for row in pressure_data[i]:
                        avg_press_summary.append({
                            "finger": finger,
                            "pressure": row[1],
                            "timestamp": row[0]
                        })
                
                summary_avg_file = summary_statistical_path / f"resumo_dados_media_pressao.csv"#create file for session data
                with open(summary_avg_file, "w", newline='') as file:#write session file
                    fieldNames = ["finger","pressure","timestamp"]
                    writer = csv.DictWriter(file,fieldNames)
                    writer.writeheader()
                    writer.writerows(avg_press_summary)

                avg_uses_array = data["summary_data"][4:6]
                total_avg_pressure_map = []
                for i, finger in enumerate(fingers):
                    press = avg_uses_array[0][i]
                    uses = avg_uses_array[1][i]

                    if press is not False and uses is False:
                        continue
                    
                    total_avg_pressure_map.append({
                        "finger": finger,
                        "total_avg_pressure": press if press is not False else None,
                        "total_uses": uses if uses is not False else None
                    })
                summary_rest_file = summary_statistical_path / "Resumo_dados_media_e_total_de_usos.csv" 
                with open(summary_rest_file, "w", newline='') as file:
                    fieldNames = ["finger","total_avg_pressure","total_uses"]
                    writer = csv.DictWriter(file,fieldNames)
                    writer.writeheader()
                    writer.writerows(total_avg_pressure_map)
            except Exception as e:
                logger.error(f"Erro ao exportar arquivos: {e}")
                self.exportError.emit(True)
            finally:
                self.exportEnd.emit(True)
