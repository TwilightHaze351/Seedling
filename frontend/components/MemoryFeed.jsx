import React from 'react';

function MemoryFeed() {
    const memories = ["User felt sad", "User asked a curious question"];

    return (
        <div className="mt-4">
            <h2 className="text-xl font-semibold">Memory Feed</h2>
            <ul>
                {memories.map((memory, index) => <li key={index}>{memory}</li>)}
            </ul>
        </div>
    );
}

export default MemoryFeed;

