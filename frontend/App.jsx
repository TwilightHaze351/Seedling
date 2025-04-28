import React, { useState } from 'react';
import ChatBox from './components/ChatBox';
import TraitViewer from './components/TraitViewer';
import MemoryFeed from './components/MemoryFeed';

function App() {
    return (
        <div className="p-4">
            <h1 className="text-2xl font-bold">Seedling</h1>
            <ChatBox />
            <TraitViewer />
            <MemoryFeed />
        </div>
    );
}

export default App;

