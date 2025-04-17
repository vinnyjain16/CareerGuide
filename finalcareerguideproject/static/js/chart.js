/**
 * JavaScript for chart visualizations throughout the CareerGuide platform
 */

/**
 * Create a radar chart for the assessment results
 * @param {string} canvasId - The ID of the canvas element for the chart
 * @param {Object} scores - Object containing the scores data
 */
function createRadarChart(canvasId, scores) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    // Extract data from scores
    const labels = Object.keys(scores);
    const data = Object.values(scores);
    
    return new Chart(ctx, {
        type: 'radar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Your Aptitude Profile',
                data: data,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                pointBackgroundColor: 'rgba(54, 162, 235, 1)',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: 'rgba(54, 162, 235, 1)'
            }]
        },
        options: {
            scales: {
                r: {
                    angleLines: {
                        display: true
                    },
                    suggestedMin: 0,
                    suggestedMax: 5
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

/**
 * Create a bar chart for comparing multiple assessment results
 * @param {string} canvasId - The ID of the canvas element for the chart
 * @param {Array} assessments - Array of assessment objects with date and scores
 */
function createComparisonChart(canvasId, assessments) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    // Prepare datasets
    const datasets = assessments.map((assessment, index) => {
        const colors = [
            { bg: 'rgba(54, 162, 235, 0.7)', border: 'rgba(54, 162, 235, 1)' },
            { bg: 'rgba(153, 102, 255, 0.7)', border: 'rgba(153, 102, 255, 1)' },
            { bg: 'rgba(255, 159, 64, 0.7)', border: 'rgba(255, 159, 64, 1)' }
        ];
        
        return {
            label: `${assessment.date}${index === 0 ? ' (Latest)' : ''}`,
            data: Object.values(assessment.scores),
            backgroundColor: colors[index].bg,
            borderColor: colors[index].border,
            borderWidth: 1
        };
    });
    
    return new Chart(ctx, {
        type: 'bar',
        data: {
            labels: Object.keys(assessments[0].scores),
            datasets: datasets
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 5
                }
            }
        }
    });
}

/**
 * Create a doughnut chart showing match percentage for career recommendations
 * @param {string} canvasId - The ID of the canvas element for the chart
 * @param {number} matchScore - The match percentage (0-100)
 */
function createMatchChart(canvasId, matchScore) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    return new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Match', 'Gap'],
            datasets: [{
                data: [matchScore, 100 - matchScore],
                backgroundColor: [
                    'rgba(54, 162, 235, 0.8)',
                    'rgba(220, 220, 220, 0.3)'
                ],
                borderColor: [
                    'rgba(54, 162, 235, 1)',
                    'rgba(220, 220, 220, 0.5)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            cutout: '75%',
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    enabled: false
                }
            }
        }
    });
}

/**
 * Create a horizontal bar chart for displaying aptitude relevance scores
 * @param {string} canvasId - The ID of the canvas element for the chart
 * @param {Object} relevanceScores - Object containing aptitude relevance scores
 */
function createRelevanceChart(canvasId, relevanceScores) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    // Extract data from relevance scores
    const labels = Object.keys(relevanceScores);
    const data = Object.values(relevanceScores);
    
    return new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                axis: 'y',
                label: 'Relevance Score',
                data: data,
                backgroundColor: 'rgba(54, 162, 235, 0.7)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            indexAxis: 'y',
            scales: {
                x: {
                    beginAtZero: true,
                    max: 5
                }
            }
        }
    });
}

// Helper function to get color based on score
function getScoreColor(score, alpha = 1) {
    if (score >= 4) {
        return `rgba(40, 167, 69, ${alpha})`;  // Green
    } else if (score >= 2.5) {
        return `rgba(255, 193, 7, ${alpha})`;  // Yellow
    } else {
        return `rgba(220, 53, 69, ${alpha})`;  // Red
    }
}

/**
 * Create a comparison chart for user aptitudes vs. career relevance
 * @param {string} canvasId - The ID of the canvas element for the chart
 * @param {Object} userScores - Object containing user's aptitude scores
 * @param {Object} relevanceScores - Object containing career's aptitude relevance scores
 */
function createAptitudeComparisonChart(canvasId, userScores, relevanceScores) {
    const ctx = document.getElementById(canvasId).getContext('2d');
    
    // Extract data
    const labels = Object.keys(userScores);
    const userData = Object.values(userScores);
    const relevanceData = Object.values(relevanceScores);
    
    return new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Your Aptitude',
                    data: userData,
                    backgroundColor: 'rgba(54, 162, 235, 0.7)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1
                },
                {
                    label: 'Career Relevance',
                    data: relevanceData,
                    backgroundColor: 'rgba(255, 99, 132, 0.7)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 5,
                    title: {
                        display: true,
                        text: 'Score (1-5)'
                    }
                }
            }
        }
    });
}
