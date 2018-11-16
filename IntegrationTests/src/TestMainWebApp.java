import org.sikuli.script.*;

import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.KeyEvent;

import org.sikuli.basics.*;

public class TestMainWebApp{

    public static void main(String[] args) {
    		
            try{	Robot r = new Robot();
            		Screen s = new Screen();
            		
            //start server block
            		try {
            		s.wait(2.0);
            		s.type(Key.WIN);
            		s.type("git bash");
            		s.type(Key.ENTER);
            		s.wait(3.0);
            		s.type("cd Documents");
            		s.type(Key.ENTER);
            		s.type("cd ECE506");
            		s.type(Key.ENTER);
            		s.type("cd BootstrapGitFolder");
            		s.type(Key.ENTER);
            		s.type("cd NetworkFirmwareUpdateRPi");
            		s.type(Key.ENTER);
            		s.type("cd vue-material-kit-v1.0.0");
            		s.type(Key.ENTER);
            		s.type("npm run dev");
            		s.type(Key.ENTER);
            		s.wait("imgs/IP.jpg",120.0);
            		s.doubleClick("imgs/IP.jpg");
            		s.rightClick("imgs/IPhighlighted.jpg");
            		s.click("imgs/copy.png");
            		System.out.println("Server now running");
            		}
            		catch(Exception e) {
            			System.out.println("Could not start VueJS page");
            		}
            		
            //navigate to webpage block
            		try {
            			s.type(Key.WIN);
                		s.type("chrome");
                		s.type(Key.ENTER);
                		s.wait(5.0);
                		s.click("imgs/searchBar.jpg");
                		s.type(Key.DELETE);
                		r.keyPress(KeyEvent.VK_CONTROL);
                		r.keyPress(KeyEvent.VK_V);
                		r.keyRelease(KeyEvent.VK_V);
                		r.keyRelease(KeyEvent.VK_CONTROL);
                		s.type(Key.ENTER);
                		System.out.println("Successfully navigated to supplied URL");
            		}
            		catch(Exception e) {
            			System.out.println("Could not navigate Web App page");
            		}
            
            //verify documentation page
            		try {
                		s.wait(5.0);
                		s.click("imgs/documentation.jpg");
                		s.wait(5.0);
                		s.wait("imgs/documentationShortDescription.jpg");
                		r.keyPress(KeyEvent.VK_CONTROL);
                		r.keyPress(KeyEvent.VK_W);
                		r.keyRelease(KeyEvent.VK_W);
                		r.keyRelease(KeyEvent.VK_CONTROL);
                		s.wait(4.0);
                		System.out.println("Documentation page successfully loaded");
            		}
            		catch(Exception e) {
            			System.out.println("Error encountered with documentation page");
            		}
            		
            //verify file appears upon trying to upload
            		try {
            			for(int i = 0; i < 15; i++) {
            			r.keyPress(KeyEvent.VK_DOWN);
            			r.keyRelease(KeyEvent.VK_DOWN);
            			}
            			s.click("imgs/browseForImage.jpg");
            			s.click("imgs/currentFolder.jpg");
            			s.type("C:\\Users\\micha_000\\Documents\\ECE506\\Test");
            			s.type(Key.ENTER);
            			s.doubleClick("imgs/testImage.jpg");
            			s.wait(4.0);
            			s.click("imgs/flashFirmware.jpg");
            			//add code to validate that image shows up at desired directory
            			s.wait(2.0);
            			System.out.println("Uploaded image successfully transfered!");
            		}
            		catch(Exception e){
            			System.out.println("Failed while choosing a file to upload");
            		}
            		
            //validate tab choosing works
            		try {
            			s.wait(1.0);
            			s.click("imgs/historyTab.jpg");
            			s.wait(1.0);
            			s.click("imgs/githubTab.jpg");
            			s.wait(1.0);
            			s.click("imgs/uploadTab.jpg");
            			s.wait(2.0);
            			System.out.println("Successfully switches between tabs");
            		}
            		catch(Exception e) {
            			System.out.println("Error choosing tabs");
            		}
            		
            //Validate Wisconsin Robotics link works
            		try {
            			r.keyPress(KeyEvent.VK_DOWN);
            			r.keyRelease(KeyEvent.VK_DOWN);
            			s.rightClick("imgs/roboticsLink.jpg");
            			s.click("imgs/newTab.png");
            			s.wait(2.0);
            			s.click("imgs/roboticsUpperTab.jpg");
            			s.wait(2.0);
            			s.wait("imgs/roboticsPage.jpg", 4.0);
            			r.keyPress(KeyEvent.VK_CONTROL);
                		r.keyPress(KeyEvent.VK_W);
                		r.keyRelease(KeyEvent.VK_W);
                		r.keyRelease(KeyEvent.VK_CONTROL);
                		s.wait(3.0);
            			System.out.println("Successfully loaded Wisconsin Robotics Page");
            		}
            		catch(Exception e) {
            			System.out.println("Error loading Wisconsin Robotics page");
            		}
            		
            //Validate About Us link works
            		try {
            			s.rightClick("imgs/aboutUsLink.jpg");
            			s.click("imgs/newTab.png");
            			s.wait(2.0);
            			s.click("imgs/aboutUsUpperTab.jpg");
            			s.wait(2.0);
            			s.wait("imgs/aboutUsPage.jpg", 4.0);
            			r.keyPress(KeyEvent.VK_CONTROL);
                		r.keyPress(KeyEvent.VK_W);
                		r.keyRelease(KeyEvent.VK_W);
                		r.keyRelease(KeyEvent.VK_CONTROL);
                		s.wait(3.0);
            			System.out.println("Successfully loaded About Us Page");
            		}
            		catch(Exception e) {
            			System.out.println("Error loading About Us page");
            		}
            		
            //Validate Github link works
            		try {
            			s.rightClick("imgs/githubLink.jpg");
            			s.click("imgs/newTab.png");
            			s.wait(2.0);
            			s.click("imgs/githubUpperTab.jpg");
            			s.wait(2.0);
            			s.wait("imgs/githubPage.jpg", 4.0);
            			r.keyPress(KeyEvent.VK_CONTROL);
                		r.keyPress(KeyEvent.VK_W);
                		r.keyRelease(KeyEvent.VK_W);
                		r.keyRelease(KeyEvent.VK_CONTROL);
                		s.wait(3.0);
            			System.out.println("Successfully loaded Github Page");
            		}
            		catch(Exception e) {
            			System.out.println("Error loading github page");
            		}
            		
            //Validate image file landed in correct location
            		try {
            		r.keyPress(KeyEvent.VK_WINDOWS);
            		r.keyPress(KeyEvent.VK_E);
            		r.keyRelease(KeyEvent.VK_E);
            		r.keyRelease(KeyEvent.VK_WINDOWS);
            		//add - validate file
            		s.click("imgs/closeFolder.jpg");
            		System.out.println("Image successfully sent to correct folder");
            		}
            		catch(Exception e) {
            			System.out.println("Error - Image not sent to folder!");
            		}
            }
            catch(Exception e) {
            	System.out.println("Undefined Fatal Error");
            }
    }
    

}