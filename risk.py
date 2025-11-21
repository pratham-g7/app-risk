def risk_score(
    title_distance: float,   
    icon_similarity: float, 
    dev_mismatch: float,      
    install_factor: float,     
    weights: dict = {}
) -> float:
    """
    Get risk score (0 = safe, 1 = high risk).
    
    title_distance: normalized Levenshtein distance (0 exact, 1 completely different)
    dev_mismatch: 0 (same dev) or 1 (different dev)
    icon_similarity: 0-1 (1 = identical icon)
    install_factor: 0-1 (1 = very low installs relative to official)
    weights: optional dict to adjust factor importance
    """

    if not weights:
        weights = {
            "title": 0.4,
            "dev": 0.3,
            "icon": 0.2,
            "install": 0.1
        }

    icon_score = 1.0 - icon_similarity

    risk = (
        weights["title"] * title_distance +
        weights["dev"] * dev_mismatch +
        weights["icon"] * icon_score +
        weights["install"] * install_factor
    )

    return min(max(risk, 0.0), 1.0)