<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

// Define Tetris block shapes and colors with subtle, semi-transparent colors
const SHAPES = [
  // I-piece
  {
    shape: [
      [1, 1, 1, 1]
    ],
    color: 'rgba(91, 108, 255, 0.40)' // brand palette
  },
  // J-piece
  {
    shape: [
      [1, 0, 0],
      [1, 1, 1]
    ],
    color: 'rgba(27, 42, 107, 0.45)' // brand palette
  },
  // L-piece
  {
    shape: [
      [0, 0, 1],
      [1, 1, 1]
    ],
    color: 'rgba(124, 137, 255, 0.35)' // brand palette
  },
  // O-piece
  {
    shape: [
      [1, 1],
      [1, 1]
    ],
    color: 'rgba(47, 75, 196, 0.42)' // brand palette
  },
  // S-piece
  {
    shape: [
      [0, 1, 1],
      [1, 1, 0]
    ],
    color: 'rgba(70, 88, 232, 0.40)' // brand palette
  },
  // T-piece
  {
    shape: [
      [0, 1, 0],
      [1, 1, 1]
    ],
    color: 'rgba(91, 108, 255, 0.34)' // brand palette
  },
  // Z-piece
  {
    shape: [
      [1, 1, 0],
      [0, 1, 1]
    ],
    color: 'rgba(107, 130, 232, 0.32)' // brand palette
  }
];

// Block size in pixels
const BLOCK_SIZE = 20;
// Maximum number of blocks falling at once
const MAX_BLOCKS = 14;
// Time between new blocks (in milliseconds)
const BLOCK_INTERVAL = 1800; // was 15000ms, which left only one block on screen at a time

const blocks = ref([]);
const animationFrameId = ref(null);
const containerRef = ref(null);

// Timer for adding new blocks
const blockTimerId = ref(null);

// Generate a random Tetris block
const generateBlock = (startY = -50) => {
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
    y: startY,
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
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  // Seed a spread of blocks so the hero is populated immediately rather than
  // waiting for the interval to trickle them in one at a time.
  const h = containerRef.value?.offsetHeight || 700;
  for (let i = 0; i < 9; i++) generateBlock(Math.random() * h - 60);
  
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
