document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    
    // UI Elements
    const previewContainer = document.getElementById('preview-container');
    const imagePreview = document.getElementById('image-preview');
    const processingOverlay = document.getElementById('processing-overlay');
    const resultBox = document.getElementById('result-box');
    const captionText = document.getElementById('caption-text');
    const resetBtn = document.getElementById('reset-btn');

    // Drag & Drop visual feedback
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, preventDefaults, false);
    });

    function preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    ['dragenter', 'dragover'].forEach(eventName => {
        dropZone.addEventListener(eventName, () => dropZone.classList.add('dragover'), false);
    });

    ['dragleave', 'drop'].forEach(eventName => {
        dropZone.addEventListener(eventName, () => dropZone.classList.remove('dragover'), false);
    });

    // Handle dropped files
    dropZone.addEventListener('drop', (e) => {
        const dt = e.dataTransfer;
        const files = dt.files;
        if (files.length) handleFile(files[0]);
    }, false);

    // Handle clicked files
    fileInput.addEventListener('change', function() {
        if (this.files.length) handleFile(this.files[0]);
    });

    function handleFile(file) {
        // Ensure it's an image
        if (!file.type.startsWith('image/')) {
            alert('Please upload an image file (JPEG, PNG, etc).');
            return;
        }

        // 1. Show Preview
        const reader = new FileReader();
        reader.onload = (e) => {
            imagePreview.src = e.target.result;
            dropZone.classList.add('hidden');
            previewContainer.classList.remove('hidden');
            resultBox.classList.add('hidden');
            
            // Start the loading animation
            processingOverlay.classList.remove('hidden');
            
            // 2. Transmit to AI 
            analyzeImage(file);
        };
        reader.readAsDataURL(file);
    }

    async function analyzeImage(file) {
        const formData = new FormData();
        formData.append('image', file);

        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            // Hide processing state
            processingOverlay.classList.add('hidden');

            if (!response.ok) {
                throw new Error(data.error || 'Server error');
            }

            // Show Result
            captionText.textContent = data.caption;
            resultBox.classList.remove('hidden');

        } catch (error) {
            processingOverlay.classList.add('hidden');
            captionText.textContent = `⚠️ Error: ${error.message}`;
            captionText.style.color = '#ef4444'; // Red error text
            resultBox.classList.remove('hidden');
        }
    }

    // Reset the UI
    resetBtn.addEventListener('click', () => {
        fileInput.value = '';
        dropZone.classList.remove('hidden');
        previewContainer.classList.add('hidden');
        resultBox.classList.add('hidden');
        captionText.style.color = ''; // Reset color
    });
});
