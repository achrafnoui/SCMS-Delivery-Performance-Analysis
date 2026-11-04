# SCMS Delivery History — Dataset Introduction

## What does this dataset represent?

This dataset contains **10,324 records and 33 columns**, covering supply-chain transactions from approximately **2006 to 2015**. It includes 43 destination countries, 73 vendors, 88 manufacturing sites, and 184 distinct products.

It is a historical record of medical-commodity transactions and deliveries. Each record brings together information about the project, product, supplier, order, fulfillment method, transportation, delivery dates, and costs.

The purpose of this analysis is to understand how these transactions moved through the supply chain, whether deliveries arrived as planned, and what operational or cost factors may be associated with performance.

## The journey behind each record

Imagine a health program needs medical supplies for a destination country. The organization identifies the project and products required, obtains a quotation, places an order, selects a supplier and fulfillment method, arranges transportation, and tracks the delivery. The dataset captures information from these different parts of that process.

### 1. Identify the transaction and destination

- `id` — unique identifier for the dataset record; it is not an order or shipment number.
- `project_code` — the project or program associated with the transaction.
- `country` — the destination country receiving the commodities.
- `managed_by` — the SCMS office responsible for managing the transaction.

Together, these fields tell us which record we are examining, which program it supports, where the goods are going, and which office manages the transaction.

### 2. Record the quotation and product requirement

- `pq_number` — reference for the price-quotation process.
- `pq_first_sent_to_client_date` — when the first quotation was sent to the client. Some entries are business-status values, such as `Pre-PQ Process` or `Date Not Captured`, rather than dates.
- `product_group` — broad product category, such as ARV.
- `sub_classification` — a more specific category, such as Adult or Pediatric.
- `item_description` — detailed description of the product.
- `molecule_test_type` — active molecule or diagnostic test type.
- `brand` — product brand or generic designation.
- `dosage` — product strength or concentration.
- `dosage_form` — physical form, such as tablet, capsule, or oral solution.
- `first_line_designation` — whether the product is designated as a first-line treatment/product.
- `unit_of_measure_per_pack` — number of individual units contained in one pack.

These fields describe what the organization intends to procure, from the broad product category down to the product's formulation and pack size.

### 3. Identify the supplier, order, and fulfillment method

- `vendor` — supplier responsible for providing the commodity.
- `manufacturing_site` — facility where the product was manufactured.
- `vendor_inco_term` — commercial term defining agreed responsibilities between buyer and seller for delivery, transport, and risk.
- `po_so_number` — Purchase Order (PO) or Sales Order (SO) reference. The source documentation associates PO with Direct Drop and SO with orders fulfilled from an RDC.
- `po_sent_to_vendor_date` — date the purchase order was sent to the vendor. Some entries contain statuses such as `N/A - From RDC`.
- `fulfill_via` — how the order is supplied: **Direct Drop** (vendor to destination) or **From RDC** (stock supplied through a Regional Distribution Center).

A vendor and a manufacturing site are not necessarily the same thing: one identifies the supplier, while the other identifies where the product was made. Likewise, `fulfill_via` describes the supply route, while the transport method is recorded separately.

### 4. Describe the shipment and its costs

- `shipment_mode` — physical transport method, such as Air, Air Charter, Truck, or Ocean.
- `asn_dn_number` — shipment/delivery document reference: Advanced Shipping Notice (ASN) or Delivery Note (DN).
- `line_item_quantity` — quantity ordered for the product line.
- `pack_price` — price of one pack.
- `unit_price` — price of an individual unit according to the dataset's unit-price definition.
- `line_item_value` — total monetary value of the product line.
- `weight_kg` — recorded shipment weight in kilograms.
- `freight_cost_usd` — recorded freight/transportation cost in US dollars when a numeric amount is available.
- `line_item_insurance_usd` — insurance cost associated with the product line, in US dollars.

Some `weight_kg` entries contain `Weight Captured Separately`, rather than a numeric weight. Similarly, `freight_cost_usd` can contain notes or references such as `Freight Included in Commodity Cost` or `Invoiced Separately`. These are meaningful business statuses, not numeric costs, and should not automatically be converted to zero.

### 5. Compare planned delivery with actual delivery

- `scheduled_delivery_date` — date the shipment was expected to reach the client.
- `delivered_to_client_date` — date the shipment was actually delivered to the client.
- `delivery_recorded_date` — date the delivery was recorded in the system.

Comparing `delivered_to_client_date` with `scheduled_delivery_date` allows us to calculate delivery variance and identify whether a shipment was early, on time, or late.

`delivery_recorded_date` represents a separate administrative event. For example, a shipment could reach the client on April 19 but only be recorded in the system on April 21. The difference may indicate reporting lag; it is not transportation delay.

## Why these fields matter to the analysis

Together, the 33 columns allow us to investigate practical management questions:

- **Delivery performance:** Are shipments arriving by their scheduled dates? Do delays vary by country, vendor, shipment mode, product, or fulfillment method?
- **Fulfillment strategy:** How do Direct Drop and From RDC compare in delivery performance and recorded logistics costs?
- **Supplier performance:** Are some vendors or manufacturing sites associated with longer delays or different cost patterns?
- **Logistics efficiency:** How do freight and insurance costs compare with the value and weight of the commodities being moved?

The dataset also contains quality limitations that must be considered before drawing conclusions. Examples include missing shipment modes, missing dosage and insurance values, and fields that mix dates or numbers with business-status text. These values must be handled carefully so that missing or separately recorded information is not mistaken for a zero or a real date.

**In short:** this dataset lets us follow medical commodities from project requirement and procurement through fulfillment and transportation to final delivery. The analysis uses that history to identify where the supply chain performs well, where delays or cost issues may exist, and which areas deserve management attention.
