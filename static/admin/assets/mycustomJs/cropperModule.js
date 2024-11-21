// cropperModule.js

function initializeCropper(imageId, aspectRatio = NaN) {
    const imageElement = document.getElementById(imageId);
    if (!imageElement) {
      console.error(`No image element found with ID ${imageId}`);
      return null;
    }
  
    // Initialize Cropper.js
    const cropper = new Cropper(imageElement, {
      aspectRatio: aspectRatio,
    });
  
    // Compress function using Compressor.js
    function compressImage(dataURL, quality = 0.7) {
      return new Promise((resolve) => {
        const imageFile = dataURLtoFile(dataURL, "cropped-image.jpg");
        new Compressor(imageFile, {
          quality: quality,
          success: (compressedBlob) => {
            resolve(URL.createObjectURL(compressedBlob));
          },
          error: (err) => {
            console.error("Compression error:", err);
            resolve(null);
          },
        });
      });
    }
  
    // Helper function to convert dataURL to File
    function dataURLtoFile(dataurl, filename) {
      const arr = dataurl.split(',');
      const mime = arr[0].match(/:(.*?);/)[1];
      const bstr = atob(arr[1]);
      let n = bstr.length;
      const u8arr = new Uint8Array(n);
      while (n--) {
        u8arr[n] = bstr.charCodeAt(n);
      }
      return new File([u8arr], filename, { type: mime });
    }
  
    // Return an object with methods to get the cropped image data, compress it, or destroy the cropper instance
    return {
      getCroppedDataURL: (type = "image/jpeg") =>
        cropper.getCroppedCanvas({ fillColor: "#fff" }).toDataURL(type),
      getCompressedCroppedDataURL: async () => {
        const croppedDataURL = cropper.getCroppedCanvas({ fillColor: "#fff" }).toDataURL("image/jpeg");
        return await compressImage(croppedDataURL);
      },
      destroy: () => cropper.destroy(),
    };
  }
  
  // Export the function as a module
  export { initializeCropper };
  