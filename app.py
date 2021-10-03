from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('DTRModel.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', output='')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict based on user inputs
    and render the result to the html page
    '''
    tahun,jeniskelamin,fasilitas,Q15,Q12,Q11,Q16,Q7,Q20,Q18,Q9,Q10,Q13 = [x for x in request.form.values()]

    data = []

    if Q15 == '1':
      data.append(1)
      Q15='Sangat Tidak Setuju'
    elif Q15 == '2':
        data.append(2)
        Q15='Tidak Setuju'
    elif Q15 == '3':
        data.append(3)
        Q15='Agak Setuju'
    elif Q15 == '4':
        data.append(4) 
        Q15='Netral'
    elif Q15 == '5':
        data.append(5) 
        Q15='Agak Setuju' 
    elif Q15 == '6':
        data.append(6)
        Q15='Setuju'  
    elif Q15 == '7':
        data.append(7)  
        Q15='Sangat Setuju'                 
    else:
        data.append(0)
        Q15='Tidak Dipilih'

    if Q20 == '1':
      data.append(1)
      Q20='Sangat Tidak Setuju'
    elif Q20 == '2':
        data.append(2)
        Q20='Tidak Setuju'
    elif Q20 == '3':
        data.append(3)
        Q20='Agak Tidak Setuju'
    elif Q20 == '4':
        data.append(4) 
        Q20='Netral'
    elif Q20 == '5':
        data.append(5)
        Q20='Agak Setuju'  
    elif Q20 == '6':
        data.append(6)
        Q20='Setuju'  
    elif Q20 == '7':
        data.append(7) 
        Q20='Sangat Setuju'                  
    else:
        data.append(0)
        Q20='Tidak Dipilih'
    
    if Q11 == '1':
      data.append(1)
      Q11='Sangat Tidak Setuju'
    elif Q11 == '2':
        data.append(2)
        Q11='Tidak Setuju'
    elif Q11 == '3':
        data.append(3)
        Q11='Agak Tidak Setuju'
    elif Q11 == '4':
        data.append(4) 
        Q11='Netral'
    elif Q11 == '5':
        data.append(5) 
        Q11='Agak Setuju' 
    elif Q11 == '6':
        data.append(6)  
        Q11='Setuju'
    elif Q11 == '7':
        data.append(7)  
        Q11='Sangat Setuju'                 
    else:
        data.append(0)
        Q11='Tidak Dipilih'

    if Q12 == '1':
      data.append(1)
      Q12='Sangat Tidak Setuju'
    elif Q12 == '2':
        data.append(2)
        Q12='Tidak Setuju'
    elif Q12 == '3':
        data.append(3)
        Q12='Agak Tidak Setuju'
    elif Q12 == '4':
        data.append(4) 
        Q12='Netral'
    elif Q12 == '5':
        data.append(5)  
        Q12='Agak Setuju'
    elif Q12 == '6':
        data.append(6)  
        Q12='Setuju'
    elif Q12 == '7':
        data.append(7)  
        Q12='Sangat Setuju'                 
    else:
        data.append(0)
        Q12='Tidak Dipilih'

    if Q16 == '1':
      data.append(1)
      Q16='Sangat Tidak Setuju'
    elif Q16 == '2':
        data.append(2)
        Q16='Tidak Setuju'
    elif Q16 == '3':
        data.append(3)
        Q16='Agak Tidak Setuju'
    elif Q16 == '4':
        data.append(4) 
        Q16='Netral'
    elif Q16 == '5':
        data.append(5)  
        Q16='Agak Setuju'
    elif Q16 == '6':
        data.append(6)  
        Q16='Setuju'
    elif Q16 == '7':
        data.append(7) 
        Q16='Sangat Setuju'                  
    else:
        data.append(0)
        Q16='Tidak Dipilih'

    if Q18 == '1':
      data.append(1)
      Q18='Sangat Tidak Setuju'
    elif Q18 == '2':
        data.append(2)
        Q18='Tidak Setuju'
    elif Q18 == '3':
        data.append(3)
        Q18='Agak Tidak Setuju'
    elif Q18 == '4':
        data.append(4) 
        Q18='Netral'
    elif Q18 == '5':
        data.append(5)  
        Q18='Agak Setuju'
    elif Q18 == '6':
        data.append(6)  
        Q18='Setuju'
    elif Q18 == '7':
        data.append(7)   
        Q18='Sangat Setuju'                
    else:
        data.append(0)
        Q18='Tidak Dipilih'

    if Q10 == '1':
      data.append(1)
      Q10='Sangat Tidak Setuju'
    elif Q10 == '2':
        data.append(2)
        Q10='Tidak Setuju'
    elif Q10 == '3':
        data.append(3)
        Q10='Agak Tidak Setuju'
    elif Q10 == '4':
        data.append(4) 
        Q10='Netral'
    elif Q10 == '5':
        data.append(5)  
        Q10='Agak Setuju'
    elif Q10 == '6':
        data.append(6)  
        Q10='Setuju'
    elif Q10 == '7':
        data.append(7)  
        Q10='Sangat Setuju'                 
    else:
        data.append(0)
        Q10='Tidak Dipilih'

    if Q7 == '1':
      data.append(1)
      Q7='Sangat Tidak Setuju'
    elif Q7 == '2':
        data.append(2)
        Q7='Tidak Setuju'
    elif Q7 == '3':
        data.append(3)
        Q7='Agak Tidak Setuju'
    elif Q7 == '4':
        data.append(4) 
        Q7='Netral'
    elif Q7 == '5':
        data.append(5) 
        Q7='Agak Setuju' 
    elif Q7 == '6':
        data.append(6)  
        Q7='Setuju'
    elif Q7 == '7':
        data.append(7)   
        Q7='Sangat Setuju'                
    else:
        data.append(0)
        Q7='Tidak Dipilih'

    if Q9 == '1':
      data.append(1)
      Q9='Sangat Tidak Setuju'
    elif Q9 == '2':
        data.append(2)
        Q9='Tidak Setuju'
    elif Q9 == '3':
        data.append(3)
        Q9='Agak Tidak Setuju'
    elif Q9 == '4':
        data.append(4)
        Q9='Netral' 
    elif Q9 == '5':
        data.append(5)  
        Q9='Agak Setuju'
    elif Q9 == '6':
        data.append(6)  
        Q9='Setuju'
    elif Q9 == '7':
        data.append(7)      
        Q9='Sangat Setuju'             
    else:
        data.append(0)
        Q9='Tidak Dipilih'

    if Q13 == '1':
      data.append(1)
      Q13='Sangat Tidak Setuju'
    elif Q13 == '2':
        data.append(2)
        Q13='Tidak Setuju'
    elif Q13 == '3':
        data.append(3)
        Q13='Agak Tidak Setuju'
    elif Q13 == '4':
        data.append(4) 
        Q13='Netral'
    elif Q13 == '5':
        data.append(5) 
        Q13='Agak Setuju' 
    elif Q13 == '6':
        data.append(6) 
        Q13='Setuju' 
    elif Q13 == '7':
        data.append(7)  
        Q13='Sangat Setuju'                 
    else:
        data.append(0)
        Q13='Tidak Dipilih'

    prediction = model.predict([data])
    if prediction == 1:
      output='Sangat Tidak Puas'
    elif prediction == 2:
      output='Tidak Puas'
    elif prediction == 3:
      output='Agak Tidak Puas'
    elif prediction == 4:
      output='Netral'
    elif prediction == 5:
      output='Agak Puas'  
    elif prediction == 6:
      output='Puas' 
    elif prediction == 7:
      output='Sangat Puas'                  
    else:
        output='Tidak Terprediksi'
    #output = round(prediction[0], 2)
    #tahun,jeniskelamin,fasilitas


    return render_template('index.html', output=output, tahun=tahun, jeniskelamin=jeniskelamin, fasilitas=fasilitas,Q15=Q15,Q20=Q20,Q11=Q11,Q12=Q12,Q16=Q16,Q18=Q18,Q10=Q10,Q7=Q7,Q9=Q9,Q13=Q13)


if __name__ == '__main__':
    app.run(debug=True)