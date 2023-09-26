
	
		
   BEGIN

		
   DROP VIEW IF EXISTS DUMMY_NON_EXISTENT_VIEW;  






















  




    
        
            
    
        
    
        
            
                
                
   CREATE OR REPLACE VIEW MATERIAL_TRACK_2_CD2ADAF8_15 AS 
SELECT
    *
FROM
    SHOPIFY_DEMO.TRACKS_2

WHERE
    
        ((
         timestamp <= '2023-09-26T07:26:31.8323Z'
        )
         OR timestamp IS NULL )
    

;  
                
            
        
    

        
    

			
    

   CREATE OR REPLACE TABLE MATERIAL_TRACK_2_VAR_TABLE_TESTHASH_15 AS (
        SELECT 
        left(sha1(random()::text),32) AS input_row_id, Material_track_2_cd2adaf8_15.*
        FROM Material_track_2_cd2adaf8_15);  



			
    
        
            
    
        
    
        
            
                
   DROP VIEW IF EXISTS MATERIAL_TRACK_2_CD2ADAF8_15;  
            
        
    

        
    
 
	
	END;  
	