from website import create_app
import numpy as np

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')                              
    