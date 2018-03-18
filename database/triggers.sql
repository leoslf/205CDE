DELIMITER $$ 

DROP TRIGGER IF EXISTS SalesOrder_after_update $$
CREATE TRIGGER SalesOrder_after_update AFTER UPDATE ON SalesOrder
FOR EACH ROW
BEGIN
    IF NEW.qty != OLD.qty OR NEW.Product_id != OLD.Product_id THEN
        UPDATE Product SET qty = qty + OLD.qty WHERE id = OLD.Product_id AND rivalry = TRUE;
        UPDATE Product SET qty = qty - NEW.qty WHERE id = NEW.Product_id AND rivalry = TRUE;
    END IF;
END $$
DELIMITER ;


