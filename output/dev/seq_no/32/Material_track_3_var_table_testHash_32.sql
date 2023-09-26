
	
		
   BEGIN

		
   DROP VIEW IF EXISTS DUMMY_NON_EXISTENT_VIEW;  






















  




    
        
            
    
        
    
        
            
                
                
   CREATE OR REPLACE VIEW MATERIAL_TRACK_3_CD2ADAF8_32 AS 
SELECT
    *
FROM
    SHOPIFY_DEMO.TRACKS_3

WHERE
    
        ((
         timestamp <= '2023-09-26T10:52:52.593652Z'
        )
         OR timestamp IS NULL )
    

;  
                
            
        
    

        
    

			
    

   CREATE OR REPLACE TABLE MATERIAL_TRACK_3_VAR_TABLE_TESTHASH_32 AS (
        SELECT 
        left(sha1(random()::text),32) AS input_row_id, Material_track_3_cd2adaf8_32.*
        FROM Material_track_3_cd2adaf8_32);  



			
    
        
            
    
        
    
        
            
                
   DROP VIEW IF EXISTS MATERIAL_TRACK_3_CD2ADAF8_32;  
            
        
    

        
    
 
	
	END;  
	