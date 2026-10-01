import matplotlib
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os
import io
import base64
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder


def generate_all_charts():
    """Generate all analytics charts and return them as base64 encoded images."""
    charts = {}
    
    # Load data
    df = pd.read_csv('model/Training.csv')
    X = df.iloc[:, 0:132]
    Y = df['prognosis']
    le = LabelEncoder()
    Y_encoded = le.fit_transform(Y)
    
    # Set seaborn style
    sns.set_theme(style="whitegrid", palette="husl")
    
    # ---- Chart 1: Disease Distribution ----
    fig, ax = plt.subplots(figsize=(14, 6))
    disease_counts = df['prognosis'].value_counts()
    sns.barplot(x=disease_counts.values, y=disease_counts.index, palette="viridis", ax=ax)
    ax.set_title('Disease Distribution in Training Dataset', fontsize=16, fontweight='bold')
    ax.set_xlabel('Number of Samples', fontsize=12)
    ax.set_ylabel('Disease', fontsize=12)
    ax.tick_params(axis='y', labelsize=8)
    plt.tight_layout()
    charts['disease_distribution'] = fig_to_base64(fig)
    plt.close(fig)
    
    # ---- Chart 2: Top 20 Most Common Symptoms ----
    fig, ax = plt.subplots(figsize=(12, 6))
    symptom_counts = X.sum().sort_values(ascending=False).head(20)
    colors = sns.color_palette("coolwarm", len(symptom_counts))
    sns.barplot(x=symptom_counts.values, y=symptom_counts.index, palette=colors, ax=ax)
    ax.set_title('Top 20 Most Frequent Symptoms Across All Diseases', fontsize=16, fontweight='bold')
    ax.set_xlabel('Frequency', fontsize=12)
    ax.set_ylabel('Symptom', fontsize=12)
    plt.tight_layout()
    charts['top_symptoms'] = fig_to_base64(fig)
    plt.close(fig)
    
    # ---- Chart 3: Symptom Correlation Heatmap (Top 15) ----
    fig, ax = plt.subplots(figsize=(10, 8))
    top_symptoms = X.sum().sort_values(ascending=False).head(15).index
    corr_matrix = X[top_symptoms].corr()
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='RdBu_r', center=0,
                square=True, linewidths=0.5, ax=ax, vmin=-1, vmax=1,
                annot_kws={"size": 7})
    ax.set_title('Symptom Correlation Heatmap (Top 15 Symptoms)', fontsize=14, fontweight='bold')
    ax.tick_params(axis='both', labelsize=8)
    plt.tight_layout()
    charts['correlation_heatmap'] = fig_to_base64(fig)
    plt.close(fig)
    
    # ---- Chart 4: Model Comparison ----
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y_encoded, test_size=0.2, random_state=42)
    
    models = {
        'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
        'Decision Tree': DecisionTreeClassifier(random_state=42),
        'KNN (k=5)': KNeighborsClassifier(n_neighbors=5),
        'Logistic Regression': LogisticRegression(max_iter=1000, random_state=42),
        'SVM (Linear)': SVC(kernel='linear', random_state=42)
    }
    
    model_accuracies = {}
    for name, model in models.items():
        model.fit(X_train, Y_train)
        Y_pred = model.predict(X_test)
        acc = accuracy_score(Y_test, Y_pred)
        model_accuracies[name] = acc
    
    fig, ax = plt.subplots(figsize=(10, 6))
    names = list(model_accuracies.keys())
    accs = [v * 100 for v in model_accuracies.values()]
    colors = ['#2ecc71' if a == max(accs) else '#3498db' for a in accs]
    bars = ax.bar(names, accs, color=colors, edgecolor='white', linewidth=1.5)
    
    for bar, acc in zip(bars, accs):
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.3,
                f'{acc:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=11)
    
    ax.set_ylim(0, 110)
    ax.set_title('Model Accuracy Comparison (5 Algorithms)', fontsize=16, fontweight='bold')
    ax.set_ylabel('Accuracy (%)', fontsize=12)
    ax.set_xlabel('Algorithm', fontsize=12)
    plt.xticks(rotation=15)
    plt.tight_layout()
    charts['model_comparison'] = fig_to_base64(fig)
    plt.close(fig)
    
    # ---- Chart 5: Symptoms per Disease Distribution ----
    fig, ax = plt.subplots(figsize=(10, 5))
    symptoms_per_disease = df.groupby('prognosis').apply(lambda x: x.iloc[:, :132].sum(axis=1).mean())
    sns.histplot(symptoms_per_disease, bins=15, kde=True, color='#e74c3c', ax=ax)
    ax.set_title('Distribution of Average Symptoms per Disease', fontsize=16, fontweight='bold')
    ax.set_xlabel('Average Number of Symptoms', fontsize=12)
    ax.set_ylabel('Count of Diseases', fontsize=12)
    plt.tight_layout()
    charts['symptoms_per_disease'] = fig_to_base64(fig)
    plt.close(fig)
    
    # ---- Chart 6: Feature Importance (Random Forest) ----
    fig, ax = plt.subplots(figsize=(12, 6))
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X, Y_encoded)
    importances = pd.Series(rf_model.feature_importances_, index=X.columns)
    top_features = importances.sort_values(ascending=False).head(20)
    sns.barplot(x=top_features.values, y=top_features.index, palette="magma", ax=ax)
    ax.set_title('Top 20 Most Important Features (Random Forest)', fontsize=16, fontweight='bold')
    ax.set_xlabel('Feature Importance Score', fontsize=12)
    ax.set_ylabel('Symptom', fontsize=12)
    plt.tight_layout()
    charts['feature_importance'] = fig_to_base64(fig)
    plt.close(fig)
    
    # Generate summary stats
    stats = {
        'total_diseases': len(df['prognosis'].unique()),
        'total_symptoms': len(X.columns),
        'total_samples': len(df),
        'best_model': max(model_accuracies, key=model_accuracies.get),
        'best_accuracy': f"{max(model_accuracies.values()) * 100:.1f}%",
        'model_accuracies': model_accuracies
    }
    
    return charts, stats


def fig_to_base64(fig):
    """Convert matplotlib figure to base64 string."""
    buf = io.BytesIO()
    fig.savefig(buf, format='png', dpi=150, bbox_inches='tight', facecolor='white')
    buf.seek(0)
    return base64.b64encode(buf.getvalue()).decode('utf-8')
