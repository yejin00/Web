var bchartArea = document.getElementById('bchart').getContext('2d');
var mchartArea = document.getElementById('mchart').getContext('2d');
var ochartArea = document.getElementById('ochart').getContext('2d');
var gchartArea = document.getElementById('gchart').getContext('2d');

var bchart = new Chart(bchartArea, {
    type: 'line',
    data: {
        labels: ['전월', '현월', '다음월'],
        datasets: [
            {
                label: '최대값',
                //data: high_list,
                data: [670, 1087, 906],
                backgroundColor: '#e24f31',
                borderColor: '#e24f31',
                borderWidth: 1,
                fill: false
            },
            {
                label: '예측값',
                data: [1000, 1600, 1500],
                backgroundColor: '#60c0ce',
                borderColor: '#60c0ce',
                borderWidth: 1,
                fill: false
            },
            {
                label: '최저값',
                data: [800, 1300, 800],
                backgroundColor: '#18b171',
                borderColor: '#18b171',
                borderWidth: 1,
                fill: false
            }
        ]
    },
    options: {
        title: {
            display: true,
            text: '배추가격'
        },
        legend: {
            position:'bottom',
            labels: {
                boxWidth: 10
            }
        },
        responsive: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                }
            }]
        },
    }
});

var mchart = new Chart(mchartArea, {
    type: 'line',
    data: {
        labels: ['전월', '현월', '다음월'],
        datasets: [
            {
                label: '최대값',
                data: [1900,  1000, 900],
                backgroundColor: '#e24f31',
                borderColor: '#e24f31',
                borderWidth: 1,
                fill: false
            },
            {
                label: '예측값',
                data: [1600, 800, 600],
                backgroundColor: '#60c0ce',
                borderColor: '#60c0ce',
                borderWidth: 1,
                fill: false
            },
            {
                label: '최저값',
                data: [1300, 600, 300],
                backgroundColor: '#18b171',
                borderColor: '#18b171',
                borderWidth: 1,
                fill: false
            }
        ]
    },
    options: {
        title: {
            display: true,
            text: '무가격'
        },
        legend: {
            position:'bottom',
            labels: {
                boxWidth: 10
            }
        },
        responsive: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                }
            }]
        },
    }
});

var ochart = new Chart(ochartArea, {
    type: 'line',
    data: {
        labels: ['전월', '현월', '다음월'],
        datasets: [
            {
                label: '최대값',
                data: [1400, 1000, 900],
                backgroundColor: '#e24f31',
                borderColor: '#e24f31',
                borderWidth: 1,
                fill: false
            },
            {
                label: '예측값',
                data: [800, 800, 600],
                backgroundColor: '#60c0ce',
                borderColor: '#60c0ce',
                borderWidth: 1,
                fill: false
            },
            {
                label: '최저값',
                data: [200, 600, 300],
                backgroundColor: '#18b171',
                borderColor: '#18b171',
                borderWidth: 1,
                fill: false
            }
        ]
    },
    options: {
        title: {
            display: true,
            text: '양파가격'
        },
        legend: {
            position:'bottom',
            labels: {
                boxWidth: 10
            }
        },
        responsive: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                }
            }]
        },
    }
});

var gchart = new Chart(gchartArea, {
    type: 'line',
    data: {
        labels: ['전월', '현월', '다음월'],
        datasets: [
            {
                label: '최대값',
                data: [1200, 1400, 1000],
                backgroundColor: '#e24f31',
                borderColor: '#e24f31',
                borderWidth: 1,
                fill: false
            },
            {
                label: '예측값',
                data: [1000, 800, 800],
                backgroundColor: '#60c0ce',
                borderColor: '#60c0ce',
                borderWidth: 1,
                fill: false
            },
            {
                label: '최저값',
                data: [800, 200, 600],
                backgroundColor: '#18b171',
                borderColor: '#18b171',
                borderWidth: 1,
                fill: false
            }
        ]
    },
    options: {
        title: {
            display: true,
            text: '건고추가격'
        },
        legend: {
            position:'bottom',
            labels: {
                boxWidth: 10
            }
        },
        responsive: false,
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                }
            }]
        },
    }
});
