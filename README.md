# 
```css
.rings {
  list-style: none;
  margin: -9.75em -20.5em;
  position: absolute;
  
  li {
    border-radius: 1em;
    font-size: 1em;
    height: 12em;
    margin-left: 1em;
    margin-top: 1em;
    position: absolute;
    width: 12em;
    
   &:before, &:after {
      border-radius: 50%;
      position: absolute;
    }
    
   &:before {
      content: "";
    }
  }
  
  li:after {
    border: 1.15em solid #000;
    bottom: 0;
    content: "";
    left: -0.1em;
    right: -0.1em;
    top: -0.1em;
  }
  
  .blue {
    left: 0;
    top: 0;
    z-index: 10;
    
   &:after {
      border-color: #0080cb;
    }
    
   +.chain {
      z-index: 24;

   &:before, &:after {
        border-bottom-color: transparent;
      }
    }
  }
  
  .yellow {
    left: 6.8em;
    top: 5.7em;
    z-index: 20;
    
 &:after {
      border-color: #fdb408;
    }
   border-right-color: transparent;
      }
    }
  }
  
  .black {
    left: 13.6em;
    top: 0;
    z-index: 21;
    
   &:after {
        border-color: #000;
    }
  }
  
  .green {
    left: 20.4em;
    top: 5.7em;
    z-index: 20;
    
   &:after {
      border-color: #00a84c;
    }
    
   +.chain  {
      z-index: 23;

   &:before, &:after {    
      top: 5.7em;
    z-index: 20;
    
   &:after {
      border-color: #00a84c;
    }
    
   +.chain  {
      z-index: 23;

   &:before, &:after {
            border-top-color:        transparent;
      }
    }
  }
  
  .red {
    left: 27.2em;
    top: 0;
    z-index: 10;
    
   &:after {
      border-color: #f02c49;
    }
    
   +.chain {
      z-index: 23;

   &:before, &:after {
        border-lef.rings {
  list-style: none;
  margin: -9.75em -20.5em;
  position: absolute;
  
  li {
    border-radius: 1em;
    font-size: 1em;
    height: 12em;
    margin-left: 1em;
    margin-top: 1em;
    position: absolute;
    width: 12em;
    
   &:before, &:after {
      border-radius: 50%;
      position: absolute;
    }
    
   &:before {
      content: "";
    }
  }
  
  li:after {
    border: 1.15em solid #000;
    bottom: 0;
    content: "";
    left: -0.1em;
    right: -0.1em;
    top: -0.1em;
  }
  
  .blue {
    left: 0;
    top: 0;
    z-index: 10;
    
   &:after {
      border-color: #0080cb;
    }
    
   +.chain {
      z-index: 24;

   &:before, &:after {
        border-bottom-color: transparent;
      }
    }
  }
  
  .yellow {
    left: 6.8em;
    top: 5.7em;
    z-index: 20;
    
 &:after {
      border-color: #fdb408;
    }
   border-right-color: transparent;
      }
    }
  }
  
  .black {
    left: 13.6em;
    top: 0;
    z-index: 21;
    
   &:after {
        border-color: #000;
    }
  }
  
  .green {
    left: 20.4em;
    top: 5.7em;
    z-index: 20;
    
   &:after {
      border-color: #00a84c;
    }
    
   +.chain  {
      z-index: 23;

   &:before, &:after {    
      top: 5.7em;
    z-index: 20;
    
   &:after {
      border-color: #00a84c;
    }
    
   +.chain  {
      z-index: 23;

   &:before, &:after {
            border-top-color:        transparent;
      }
    }
  }
  
  .red {
    left: 27.2em;
    top: 0;
    z-index: 10;
    
   &:after {
      border-color: #f02c49;
    }
    
   +.chain {
      z-index: 23;

   &:before, &:after {
        border-left-color: transparent;
      }
    }
  }  
}
t-color: transparent;
      }
    }
  }  
}














/* general styling */
:root {
  font-size: calc(1vw + 1vh + .25vmin);
}

html, body {
  height: 100%;
  margin: 0;
}

body {
  -webkit-box-align: center;
  -ms-flex-align: center;
  align-items: center;
  background-color: #fffdee;
  display: -webkit-box;
  display: -ms-flexbox;
  display: flex;
}

.container {
  margin: 0 auto;
}
```
```html
<div class="container">
  <ul class="rings">
    <li class="blue"></li>
    <li class="blue chain"></li>
    <li class="yellow"></li>
    <li class="yellow chain"></li>
    <li class="black"></li>
    <li class="green"></li>
    <li class="green chain"></li>
    <li class="red"></li>
    <li class="red chain"></li>
  </ul>
</div>
```
🏅📊 Olympic History Data Analysis 

![Olympic Analysis](https://img.shields.io/badge/Olympic-Data%20Analysis-blue?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.8%2B-yellow?style=for-the-badge) ![Data Visualization](https://img.shields.io/badge/Visualization-Powered-red?style=for-the-badge) ![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📖 Project Overview

The **Olympic History Data Analysis** project aims to explore and analyze historical Olympic Games data. This project provides insights into trends, performances, and statistics related to different sports, countries, and athletes over the years. 

🎯 **Objective**: 
To uncover patterns and insights from Olympic data that can help understand the evolution of the Games and the performances of various nations and athletes.

---

## 🌟 Features

- **Data Exploration**: In-depth analysis of Olympic data spanning over a century.
- **Trend Analysis**: Visualization of trends in medals, participation, and performances over time.
- **Country Comparisons**: Analyze and compare performances of different countries.
- **Sport-Specific Insights**: Breakdown of performances by individual sports.

---

## 🛠️ Technologies Used

- **Python 3.8+**
- **Pandas**, **Numpy** for data manipulation and analysis.
- **Matplotlib**, **Seaborn** for data visualization.
- **Jupyter Notebook** for exploratory data analysis.

---

## 📂 Project Structure

```bash
olympic-history-data-analysis/
├── data/
│   ├── olympic_data.csv      # Dataset containing Olympic historical data
├── notebooks/
│   ├── exploratory_analysis.ipynb # EDA notebook
├── visualizations/
│   ├── medal_trends.png       # Visualizations of medal trends
│   ├── country_performance.png # Visualizations comparing countries
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
```

---

## 🚀 Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/olympic-history-data-analysis.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd olympic-history-data-analysis
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Open the Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

---

## ⚙️ How It Works

### 1. Data Preprocessing 🧹
- Cleaning and preprocessing the dataset to handle missing values and format inconsistencies.
- Feature engineering to create new variables, such as total medals won by a country in each Olympic year.

### 2. Exploratory Data Analysis (EDA) 📊
- Visualizing distributions of medals by country and year.
- Analyzing trends in athlete participation and medal counts over time.

### 3. Data Visualization 🎨
- Creating impactful visualizations to represent data insights:
  - Medal distribution by country.
  - Trends in Olympic participation over the years.
  - Sports that have gained or lost popularity.

---

## 📊 Insights and Findings

- **Medal Trends**: Identify which countries dominate specific sports.
- **Participation Growth**: Examine the increase in the number of countries participating in the Olympics.
- **Event Popularity**: Analyze the rise and fall of various sports in the Olympic Games.

---

## 🎥 Demo

Explore the project and its insights through the Jupyter Notebook:

https://jgdmwmtokrgkv7purcz9ao.streamlit.app/

---

## 🤝 Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request. For major changes, please discuss them in an issue first.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

> **References**:
> - [Pandas Documentation](https://pandas.pydata.org/)
> - [Matplotlib Documentation](https://matplotlib.org/)
> - [Seaborn Documentation](https://seaborn.pydata.org/)
