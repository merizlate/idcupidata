def adjust_color_contrast(image, amount):
    # Apply color contrast adjustment
    adjusted_image = image.apply_contrast(amount)
    
    # Return the adjusted image
    return adjusted_image

# Example usage
my_image = load_image('image.jpg')
contrast_amount = -0.5  # Negative value for high contrast
adjusted_image = adjust_color_contrast(my_image, contrast_amount)
