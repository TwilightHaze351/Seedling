import React from 'react';

function TraitViewer() {
    // Hardcoded example for now
    const traits = { curiosity: 0.6, empathy: 0.7, patience: 0.5 };

    return (
        <div className="mt-4">
            <h2 className="text-xl font-semibold">Personality Traits</h2>
            {Object.entries(traits).map(([trait, value]) => (
                <div key={trait}>{trait}: {Math.round(value * 100)}%</div>
            ))}
        </div>
    );
}

export default TraitViewer;
