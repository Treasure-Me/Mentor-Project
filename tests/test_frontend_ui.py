import pytest
import time
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestFrontendUI:
    def setup_method(self):
        """Set up Chrome driver for testing"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in background
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost:5000"
    
    def teardown_method(self):
        """Clean up after tests"""
        self.driver.quit()
    
    def test_home_page_loads(self):
        """Test that home page loads with all elements"""
        self.driver.get(self.base_url)
        
        # Check page title
        assert "Matrix Multiplier Mayhem" in self.driver.title
        
        # Check main heading
        heading = self.driver.find_element(By.TAG_NAME, "h1")
        assert "Matrix Multiplier Mayhem" in heading.text
    
    def test_level_selection(self):
        """Test level selection and loading"""
        self.driver.get(self.base_url)
        
        # Find and click level selection (assuming there's a level select button/link)
        level_links = self.driver.find_elements(By.CLASS_NAME, "level-link")
        if level_links:
            level_links[0].click()
            
            # Wait for level to load
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.ID, "level-number"))
            )
            
            level_number = self.driver.find_element(By.ID, "level-number")
            assert level_number.text == "1" or "Level" in level_number.text
    
    def test_matrix_drag_and_drop(self):
        """Test drag and drop functionality for matrices"""
        self.driver.get(f"{self.base_url}/level/0")
        
        # Find draggable matrices and drop target
        draggable_matrices = self.driver.find_elements(By.CLASS_NAME, "draggable-matrix")
        drop_target = self.driver.find_element(By.ID, "transformation-slot")
        
        if draggable_matrices and drop_target.is_displayed():
            # This would require JavaScript execution for drag and drop
            # For now, we'll just verify elements exist
            assert len(draggable_matrices) > 0
            assert drop_target.is_displayed()
    
    def test_solution_verification_ui(self):
        """Test the solution verification UI flow"""
        self.driver.get(f"{self.base_url}/level/0")
        
        # Find and click verify button
        verify_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Verify')]")
        verify_button.click()
        
        # Check for feedback message
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "feedback"))
        )
        
        feedback = self.driver.find_element(By.ID, "feedback")
        assert feedback.is_displayed()
    
    def test_hint_system_ui(self):
        """Test hint system UI"""
        self.driver.get(f"{self.base_url}/level/0")
        
        # Find and click hint button
        hint_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Hint')]")
        hint_button.click()
        
        # Check that hint is displayed
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "hint-message"))
        )
        
        hint_message = self.driver.find_element(By.CLASS_NAME, "hint-message")
        assert hint_message.is_displayed()
        assert len(hint_message.text) > 0
    
    def test_game_progression(self):
        """Test moving between levels"""
        self.driver.get(f"{self.base_url}/level/0")
        
        # Complete level (this would require actually solving it)
        # For now, we'll test navigation elements exist
        
        next_level_buttons = self.driver.find_elements(By.CLASS_NAME, "next-level")
        if next_level_buttons:
            next_level_buttons[0].click()
            WebDriverWait(self.driver, 5).until(
                EC.url_contains("/level/1")
            )
            assert "level/1" in self.driver.current_url
    
    def test_responsive_design(self):
        """Test that UI is responsive"""
        self.driver.get(self.base_url)
        
        # Test different screen sizes
        sizes = [(1200, 800), (768, 1024), (375, 667)]  # desktop, tablet, mobile
        
        for width, height in sizes:
            self.driver.set_window_size(width, height)
            
            # Check that main container is visible and properly sized
            container = self.driver.find_element(By.CLASS_NAME, "game-container")
            assert container.is_displayed()
            
            # Take screenshot for visual verification (optional)
            # self.driver.save_screenshot(f"layout_{width}x{height}.png")
    
    def test_matrix_visualization(self):
        """Test that matrices are properly displayed"""
        self.driver.get(f"{self.base_url}/level/0")
        
        # Check input matrix display
        input_matrix = self.driver.find_element(By.ID, "input-matrix")
        assert input_matrix.is_displayed()
        
        # Check matrix cells exist
        matrix_cells = self.driver.find_elements(By.CLASS_NAME, "matrix-cell")
        assert len(matrix_cells) > 0
        
        # Verify matrix dimensions are shown
        dimension_elements = self.driver.find_elements(By.CLASS_NAME, "matrix-dimensions")
        if dimension_elements:
            for dim in dimension_elements:
                assert "×" in dim.text  # Should contain dimension separator
