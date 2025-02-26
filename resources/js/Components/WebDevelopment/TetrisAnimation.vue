<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

// Define Tetris block shapes and colors with subtle, semi-transparent colors
const SHAPES = [
  // I-piece
  {
    shape: [
      [1, 1, 1, 1]
    ],
    color: 'rgba(59, 130, 246, 0.5)' // Blue-500 with low opacity
  },
  // J-piece
  {
    shape: [
      [1, 0, 0],
      [1, 1, 1]
    ],
    color: 'rgba(30, 64, 175, 0.5)' // Blue-800 with low opacity
  },
  // L-piece
  {
    shape: [
      [0, 0, 1],
      [1, 1, 1]
    ],
    color: 'rgba(96, 165, 250, 0.5)' // Blue-400 with low opacity
  },
  // O-piece
  {
    shape: [
      [1, 1],
      [1, 1]
    ],
    color: 'rgba(37, 99, 235, 0.5)' // Blue-600 with low opacity
  },
  // S-piece
  {
    shape: [
      [0, 1, 1],
      [1, 1, 0]
    ],
    color: 'rgba(79, 70, 229, 0.5)' // Indigo-600 with low opacity
  },
  // T-piece
  {
    shape: [
      [0, 1, 0],
      [1, 1, 1]
    ],
    color: 'rgba(99, 102, 241, 0.5)' // Indigo-500 with low opacity
  },
  // Z-piece
  {
    shape: [
      [1, 1, 0],
      [0, 1, 1]
    ],
    color: 'rgba(129, 140, 248, 0.5)' // Indigo-400 with low opacity
  }
];

// Block size in pixels
const BLOCK_SIZE = 20;
// Maximum number of blocks falling at once
const MAX_BLOCKS = 6;
// Time between new blocks (in milliseconds)
const BLOCK_INTERVAL = 15000; // One block every 8 seconds

const blocks = ref([]);
const animationFrameId = ref(null);
const containerRef = ref(null);

// Timer for adding new blocks
const blockTimerId = ref(null);

// Generate a random Tetris block
const generateBlock = () => {
  if (blocks.value.length >= MAX_BLOCKS) return;
  
  const containerWidth = containerRef.value?.offsetWidth || 200;
  const shapeIndex = Math.floor(Math.random() * SHAPES.length);
  const shape = SHAPES[shapeIndex];
  const shapeWidth = shape.shape[0].length * BLOCK_SIZE;
  
  // Random x position within container width
  const x = Math.floor(Math.random() * (containerWidth - shapeWidth));
  
  blocks.value.push({
    id: Date.now() + Math.random(),
    shape: shape.shape,
    color: shape.color,
    x: x,
    y: -50, // Start just above the visible area
    speed: 0.3 + Math.random() * 0.5, // Slower, more consistent speed
    rotation: Math.floor(Math.random() * 4) // Random rotation (0, 1, 2, or 3)
  });
};

// Update block positions
const updateBlocks = () => {
  const containerHeight = containerRef.value?.offsetHeight || 800;
  
  blocks.value.forEach(block => {
    block.y += block.speed;
  });
  
  // Remove blocks that have fallen out of view
  blocks.value = blocks.value.filter(block => {
    const blockHeight = block.shape.length * BLOCK_SIZE;
    return block.y < containerHeight;
  });
  
  animationFrameId.value = requestAnimationFrame(updateBlocks);
};

// Rotate a shape matrix
const rotateShape = (shape, rotation) => {
  if (rotation === 0) return shape;
  
  let rotated = shape;
  for (let i = 0; i < rotation; i++) {
    rotated = rotateMatrix(rotated);
  }
  return rotated;
};

// Rotate a matrix 90 degrees clockwise
const rotateMatrix = (matrix) => {
  const rows = matrix.length;
  const cols = matrix[0].length;
  const result = Array(cols).fill().map(() => Array(rows).fill(0));
  
  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      result[c][rows - 1 - r] = matrix[r][c];
    }
  }
  
  return result;
};

onMounted(() => {
  // Generate initial block
  generateBlock();
  
  // Start animation
  updateBlocks();
  
  // Set up interval to add new blocks
  blockTimerId.value = setInterval(() => {
    if (blocks.value.length < MAX_BLOCKS) {
      generateBlock();
    }
  }, BLOCK_INTERVAL);
});

onUnmounted(() => {
  // Clean up animation frame and timer
  if (animationFrameId.value) {
    cancelAnimationFrame(animationFrameId.value);
  }
  
  if (blockTimerId.value) {
    clearInterval(blockTimerId.value);
  }
});
</script>

<template>
  <div ref="containerRef" class="tetris-container">
    <div v-for="block in blocks" :key="block.id" class="tetris-block" :style="{
      left: `${block.x}px`,
      top: `${block.y}px`
    }">
      <div v-for="(row, rowIndex) in rotateShape(block.shape, block.rotation)" :key="`row-${rowIndex}`" class="tetris-row">
        <div v-for="(cell, cellIndex) in row" :key="`cell-${cellIndex}`" 
             class="tetris-cell" 
             :style="{ 
               backgroundColor: cell ? block.color : 'transparent',
               width: `${BLOCK_SIZE}px`, 
               height: `${BLOCK_SIZE}px` 
             }">
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.tetris-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  pointer-events: none; /* Allow clicks to pass through */
}

.tetris-block {
  position: absolute;
  transform: translate3d(0, 0, 0); /* Hardware acceleration */
}

.tetris-row {
  display: flex;
}

.tetris-cell {
  box-sizing: border-box;
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 0 1px rgba(255, 255, 255, 0.05);
}
</style>
