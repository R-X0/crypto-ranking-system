import matplotlib.pyplot as plt
from io import BytesIO
import base64

class ChartGenerator:
    @staticmethod
    def generate_ranking_chart(coin_symbol, ranking_data):
        timestamps, ranks = zip(*ranking_data)
        
        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, ranks, marker='o')
        plt.title(f"Ranking Trend for {coin_symbol}")
        plt.xlabel("Date")
        plt.ylabel("Rank")
        plt.gca().invert_yaxis()  # Invert y-axis so that rank 1 is at the top
        
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        
        graphic = base64.b64encode(image_png)
        graphic = graphic.decode('utf-8')
        
        return f"<img src='data:image/png;base64,{graphic}'>"